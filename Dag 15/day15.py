from aoc import read_input,list2grid

# input
lines = read_input("inputdag15")

# part 1
grid = list2grid(lines[:50])
moves = ''.join(lines[51:])
        
robot = [pos for pos,key in grid.items() if key == '@'][0]

right = lambda x,y: (x+1,y)
left = lambda x,y: (x-1,y)
up = lambda x,y: (x,y-1)
down = lambda x,y: (x,y+1)
step = {'^':up,'<':left,'>':right,'v':down}
    
for move in moves:
    new_robot = step[move](*robot)
    move_blocks = []
    while True:
        if grid[new_robot] == 'O':
            move_blocks.append(new_robot)
        else:
            break
        new_robot = step[move](*new_robot)
    
    if grid[new_robot] == '.' and not move_blocks:
        grid[robot] = '.'
        robot = new_robot
    elif grid[new_robot] == '.' and move_blocks:
        for block in move_blocks:
            grid[step[move](*block)] = 'O'
        grid[robot] = '.'
        robot = move_blocks[0]
        grid[robot] = '@'

        
print(sum(100*y+x for (x,y),key in grid.items() if key == 'O'))


# part 2
grid = list2grid(lines[:50])
moves = ''.join(lines[51:])
extended_grid = {}
robot = [pos for pos,key in grid.items() if key == '@'][0]
  
for pos,value in grid.items():
    x,y = pos
    if value == '#' or value == '.':
        extended_grid[(2*x,y)] = value
        extended_grid[(2*x+1,y)] = value
    elif value == 'O':
        extended_grid[(2*x,y)] = '['
        extended_grid[(2*x+1,y)] = ']'
    elif value == '@':
        extended_grid[(2*x,y)] = '@'
        extended_grid[(2*x+1,y)] = '.'
    
for i,move in enumerate(moves):
    robot = [pos for pos,key in extended_grid.items() if key == '@'][0]
    stop = False
    if move in ('v','^'):
        complete_border = set([robot])
        all_borders = []
        while not stop:
            complete_border = list(set(complete_border))
            all_borders.append(complete_border)
            new_border =[]
            for border in complete_border:
                border = step[move](*border)
                if extended_grid[border] == '[':
                    new_border.append(border)
                    new_border.append(right(*border))
                elif extended_grid[border] == ']':
                    new_border.append(border)
                    new_border.append(left(*border))
                elif extended_grid[border] == '#':
                    stop = True
                    break
            else:
                if new_border:
                    complete_border = new_border
                else:
                    break
            
        if not stop: 
            for border in all_borders[::-1]:
                for pos in border:
                    extended_grid[step[move](*pos)] =extended_grid[pos]
                    extended_grid[pos] = '.'
    else:
        move_robot = robot
        all_moves = []
        while not stop:
            all_moves.append(move_robot)
            move_robot = step[move](*move_robot)
            if extended_grid[move_robot] == '.':
                break
            elif extended_grid[move_robot] == '#':
                stop = True
                
        if not stop: 
            for pos in all_moves[::-1]:
                extended_grid[step[move](*pos)] = extended_grid[pos]
                extended_grid[pos] = '.'

print(sum(100*y+x for (x,y),key in extended_grid.items() if key == '['))

                
        
    
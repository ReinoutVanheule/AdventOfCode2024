from aoc import read_input, list2grid

# input
lines = read_input("inputdag6")

# part 1
grid = list2grid(lines)
grid = {complex(pos[0],pos[1]):value for pos,value in grid.items()}

start = [pos for pos,value in grid.items() if value == '^'][0]
move = complex(0,-1)
path =  [(start,move)]
grid[start] = '.'
current = start

while current+move in grid:
    if grid[current+move] == '.':
        current += move
        path.append((current,move))
    else:
        move *= complex(0,1)
print(len(set(c for c,m in path)))


# part 2
total_loop = 0
seen = set()
for i,(pos,_) in enumerate(path[1:]):
    if pos not in seen:
        new_path = []
        grid[pos] = '#'
        current,move = path[i]
        
        while current+move in grid:
            if grid[current+move] == '.':
                current += move
                if ((current,move) in new_path):
                    total_loop += 1
                    break
                else:
                    new_path.append((current,move))
            else:
                move *= complex(0,1)
        
        grid[pos] = '.'
        seen.add(pos)
print(total_loop)

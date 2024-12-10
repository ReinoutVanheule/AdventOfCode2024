from aoc import read_input,list2grid

# input
lines = read_input("inputdag10")
grid ={complex(key[0],key[1]):int(value) for key,value in list2grid(lines).items()}          
trailheads = [pos for pos,key in grid.items() if key == 0]

def explore(trailhead):
    all_endings = []
    def move_one_step(position,step):
        if step == 10:
            all_endings.append(position)
        else:
            for move in (-1,+1,+1j,-1j):
                if grid.get(position+move)==step:
                    move_one_step(position+move,step+1)
    move_one_step(trailhead,1)
    return len(set(all_endings)),len(all_endings)

total_part1 = total_part2 = 0
for trailhead in trailheads:
    a,b = explore(trailhead)
    total_part1 += a
    total_part2 += b
   
# part 1    
print(total_part1)

# part 2
print(total_part2)

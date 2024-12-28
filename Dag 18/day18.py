from aoc import read_input,neighbours
from collections import deque

# input
lines = read_input("inputdag18")

# part 1
grid = {}
for i in range(71):
    for j in range(71):
        grid[(i,j)] = '.'

for line in lines[:1024]:
    grid[tuple(map(int,line.split(',')))] = '#'
    
def find_path(grid,start,end):
    explore = deque([(start,0)])
    seen = set()
    while explore:
        pos,step = explore.popleft()
        if pos == end:
            return step
        for neighbour in neighbours(*pos,4):
            if neighbour not in seen and grid.get(neighbour) == '.':
                explore.append((neighbour,step+1))
                seen.add(neighbour)
    return -1

print(find_path(grid,(0,0),(70,70)))

# part 2
for line in lines[1024:len(lines)]:
    key = tuple(map(int,line.split(',')))
    grid[key] = '#'
    if find_path(grid,(0,0),(70,70)) == -1:
        print(line)
        break
    
from aoc import read_input,list2grid,neighbours
from collections import deque

# input
lines = read_input("inputdag20")

grid = list2grid(lines)
start = [key for key,value in grid.items() if value == 'S'][0]
end = [key for key,value in grid.items() if value == 'E'][0]
grid[end] = '.'
grid[start] = '.'

def transverse(grid,start):
    distance ={}
    explore = deque([(start,0)])
    while explore:
        pos,step = explore.popleft()
        distance[pos] = step
        for neighbour in neighbours(*pos,4):
            if neighbour not in distance and grid.get(neighbour) == '.':
                explore.append((neighbour,step+1))
    return distance

distance_start = transverse(grid,start)
distance_end = transverse(grid,end)
start_to_end = distance_start[end]

# part 1 and 2
for cheat in (2,20):
    total = 0
    for key1,value1 in distance_start.items():
        for key2,value2 in distance_end.items():
            distance = abs(key1[0]-key2[0]) + abs(key1[1]-key2[1])
            if distance<=cheat and value1 + value2 + distance <=start_to_end-100:
                total += 1
    print(total)

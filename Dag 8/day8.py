from aoc import read_input,list2grid
from collections import defaultdict
from itertools import permutations

# input
lines = read_input("inputdag8")
grid =list2grid(lines)
antennas = defaultdict(list)

for key,value in grid.items():
    if value != '.':
        antennas[value].append(key)
        
antinodes = set()
def add_antinode(n1,n2,i):
    a = (n1[0]+i*(n2[0]-n1[0]),n1[1]+i*(n2[1]-n1[1]))
    return a

# part 1
for key,positions in antennas.items():
    for p1,p2 in permutations(positions,2):
        a = add_antinode(p1,p2,-1)
        antinodes.add(a)

in_grid = lambda a:a[0]>=0 and a[0]<50 and a[1]>=0 and a[1]<50
antinodes = set(filter(in_grid,antinodes))
print(len(antinodes))

# part 2
antinodes = set()
for key,positions in antennas.items():
    for p1,p2 in permutations(positions,2):
        a = p1
        i = -1
        while in_grid(a):
            antinodes.add(a)
            a = add_antinode(p1,p2,i)
            i -= 1
print(len(antinodes))

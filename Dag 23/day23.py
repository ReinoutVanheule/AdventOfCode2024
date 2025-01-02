from aoc import read_input
from itertools import combinations

# input
connections = read_input("inputdag23")

# part 1
from collections import defaultdict

computers = defaultdict(set)
for connection in connections:
    c1,c2 =  connection.split('-')
    computers[c1].add(c2)
    computers[c2].add(c1)
    
total = 0
for c1, links in computers.items():
    for c2,c3 in combinations(links,2): 
        if c2 in computers[c3]:
            if c1[0] == 't' or c2[0] == 't' or c3[0] == 't':
                total += 1
print(total//3)

# part 2
try_amount = 12
for c in computers:
    link = computers[c]
    for combination in combinations(link,try_amount):
        all_computers = combination + (c,)

        all_linked = True
        for c1 in all_computers:
            for c2 in all_computers:
                if c1 != c2 and c1 not in computers[c2]:
                    all_linked = False
                    
        if all_linked:
            print(','.join(sorted(all_computers)))



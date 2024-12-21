from aoc import read_input,list2grid,neighbours
from random import choice

# input
plants = list2grid(read_input("inputdag12"))

# part 1
all_positions = plants.keys()

def explore(position,letter):
    region = set((position,))
    
    def step(position,letter):
        region.add(position)
        for new_p in neighbours(*position):
            if new_p not in region and plants.get(new_p)==letter:
                step(new_p,letter)
    
    step(position,letter)
    return region

price_region = lambda region: sum(new_p not in region  for pos in region for new_p in neighbours(*pos))

all_regions = []
price = 0
while all_positions:
    position= choice(list(all_positions))
    region = explore(position,plants[position])
    price += len(region)*price_region(region)
    all_positions -= region
    all_regions.append(region)
print(price)

# part 2
is_neighbour = lambda pos1,pos2 : True if abs(pos1[0]-pos2[0]) == 1 and pos1[1]-pos2[1] == 0 or abs(pos1[1]-pos2[1]) == 1 and pos1[0]-pos2[0] == 0 else False

def sides(positions):
    distinct_sides = []
    
    for position in positions:
        found = False
        for side in distinct_sides:
            for side_pos in side:
                if is_neighbour(side_pos,position):
                    side.add(position)
                    found = True
                    break
        if not found:
            new_side = set((position,))
            distinct_sides.append(new_side)
            
    return len(distinct_sides)

price = 0
for region in all_regions:
    for a,b in ((0,1),(0,-1),(1,0),(-1,0)):
        border = []
        for pos in region: 
            new_pos = (pos[0]+a,pos[1]+b)
            if new_pos not in region:
                border.append(new_pos)
        price += sides(sorted(border))*len(region)
print(price)



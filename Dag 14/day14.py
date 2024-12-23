from aoc import read_input

# input
lines = read_input("inputdag14")

# part 1
lines = [[x[2:].split(',') for x in line.split()] for line in lines]

def drawing(nr_seconds):
    final_positions =[]
    for line in lines:
        (pos_x,pos_y), (vel_x,vel_y) = line
        final_x = (int(pos_x) + nr_seconds*int(vel_x)) % 101
        final_y = (int(pos_y) + nr_seconds*int(vel_y)) % 103
        final_positions.append((final_x,final_y))
    return final_positions

final_positions = drawing(100)
first =  second = third = fourth = 0
for x,y in final_positions:
    if x>50 and y<51:
        first += 1
    elif x<50 and y<51:
        second += 1 
    elif x<50 and y>51:
        third += 1
    elif x>50 and y>51:
        fourth += 1
print(first*second*third*fourth)

# part 2
nr_seconds = 0
while True:
    final_positions = drawing(nr_seconds)
    if len(set(final_positions))==500:
        print(nr_seconds)
        break
    nr_seconds += 1
        
        
        
        
        
        
    

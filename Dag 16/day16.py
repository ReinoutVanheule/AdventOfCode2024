from aoc import read_input,list2grid

# input
lines = list2grid(read_input("inputdag16"))

# part 1 and 2
lines = {complex(x,y):value for (x,y),value in lines.items()}
start = [key for key,value in lines.items() if value == 'S'][0]
end = [key for key,value in lines.items() if value == 'E'][0]
lines[end]= '.'

all_unique_positions = set([start])
start = (start,1,0,[start])
explore = [start]
all_positions = {}
all_scores =[]
while explore:
    new_explore = []
    for pos,direction,score,trail in explore:
        if pos == end:
            if score ==93436:
                all_unique_positions |= set(trail)
            all_scores.append(score)
        if score <= all_positions.get((pos,direction),10**6):
            for new_direction,new_score in zip((direction,1j*direction,-1j*direction),
                                                   (score+1,score+1001,score+1001)):
                new_trail = trail + [pos+new_direction]
                if lines.get(pos+new_direction) == '.':
                    new_explore.append((pos+new_direction,new_direction,new_score,new_trail))
            all_positions[(pos,direction)] = score
    explore = new_explore
    
print(min(all_scores))
print(len(all_unique_positions))
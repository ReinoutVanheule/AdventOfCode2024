from aoc import read_input

# input
text = read_input("inputdag5")

# part 1
rules = text[0:1176]
updates = text[1177:]

rules = [tuple(seq.split('|')) for seq in rules]
updates = [update.split(',') for update in updates]

sum1 = 0
invalid_updates = []
for update in updates:
    valid = True
    for a,b in rules:
        if a in update and b in update and update.index(a)>update.index(b):
            invalid_updates.append(update)
            break 
    else:
        sum1 += int(update[len(update)//2])
print(sum1)

# part 2
sum2 = 0
for update in invalid_updates:
    again = True
    while again:
        for a,b in rules:
            i = update.index(a) if a in update else -1
            j = update.index(b) if b in update else -1
            
            if i!=-1 and j!=-1 and i>j:
                update[i],update[j]=update[j],update[i]
                break
        else:
            again = False
    sum2 += int(update[len(update)//2])
print(sum2)
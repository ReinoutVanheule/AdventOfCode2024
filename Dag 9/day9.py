from aoc import read_input

# input
lines = read_input("inputdag9")[0]

# part 1
idblock= 0
result =[]
block = True
total_block = 0
for c in lines:
    if block:
        block  = False
        result += [idblock]*int(c)
        total_block += int(c)
        idblock += 1
    else:
        block = True
        result += [-1]*int(c)
last_id = result[-1]


insert_indexes = [i for i,c in enumerate(result) if c == -1]
for i in range(len(result)-1,0,-1):
    c = result[i]
    if insert_indexes:
        if c == -1:
            insert_indexes.remove(i)
        else:
            hole = insert_indexes[0]
            result[hole] = c
            insert_indexes = insert_indexes[1:]
    else:
        break

print(sum(i*j for i,j in zip(range(total_block),result)))

# part 2
block = True
idblocklow = 0
idblockhigh = 19998
result =[]
while True:
    l = int(lines[idblocklow])
    h = int(lines[idblockhigh])
    if block:
         result += [idblocklow]*l
         block = False
         idblocklow += 2
    else:
        if l < h:
            result += []
        
        
        
        
        
        
        
        
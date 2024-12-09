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
        result += [idblock]*int(c)
        total_block += int(c)
        idblock += 1
    else:
        result += [-1]*int(c)
    block = not block
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

# part 1
blocks = [(int(length),idblock) for length,idblock in zip(lines[::2],range(10000))]
free = [int(length) for length in lines[1::2]]
result = []
block = True
while blocks:
    first = blocks[0]
    last = blocks[-1]
    available = free[0]
    
    if block:
        result += [first[1]]*first[0]
        blocks = blocks[1:]
        block = False
    else:
        if last[0] == available:
            result += [last[1]]*last[0]
            free = free[1:]
            blocks = blocks[:-1]
            block = True
    
        elif last[0] < available:
            result += [last[1]]*last[0]
            blocks = blocks[:-1]
            free[0] = available-last[0]
            
        else:
            result += [last[1]]*available
            free = free[1:]
            blocks[-1] = (last[0]-available,last[1])
            block = True

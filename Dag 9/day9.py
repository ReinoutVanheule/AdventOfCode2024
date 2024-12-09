from aoc import read_input

# input
lines = read_input("inputdag9")[0]

# part 1
idblock= 0
result =[]
block = True
for b,f in zip(lines[::2],lines[1::2]+"0"):
    result += [idblock]*int(b)+[-1]*int(f)
    idblock += 1

insert_indexes = [i for i,c in enumerate(result) if c == -1]
i = len(result)-1
while i >= 0 and insert_indexes:
    c = result[i]
    if insert_indexes:
        if c == -1:
            insert_indexes.remove(i)
        else:
            result[insert_indexes[0]] = c
            insert_indexes.pop(0)
    i-=1

length_result = sum(map(int,lines[::2]))
print(sum(a*b for a,b in zip(range(length_result),result)))
    
# part 2
blocks = [(int(length),idblock) for length,idblock in zip(lines[::2],range(10000))]
free = [int(length) for length in lines[1::2]]
result = 20000*8*[0]
old_free = free.copy()

while len(blocks)>1:
    length,idc = blocks.pop()
    idd = sum(old_free[:idc])+sum(x for x,y in blocks[:idc])
    for i,lenempty in enumerate(free[:idc]):
        if length <= lenempty:
            idd = sum(old_free[:i])+sum(x for x,y in blocks[:i+1])+old_free[i]-free[i]
            free[i] -= length
            break
    result[idd:idd+length] = [idc]*length
        
print(sum(a*b for a,b in zip(range(len(result)),result)))

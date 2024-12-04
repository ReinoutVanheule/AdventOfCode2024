from aoc import read_input

# input
lines = read_input('inputdag1')

t1= time.time()
left =[]
right =[]

for line in lines:
    left_el,right_el= [int(el) for el in line.split()]
    left.append(left_el)
    right.append(right_el)

left.sort()
right.sort()

# part 1
print(sum(abs(el1-el2) for el1,el2 in zip(left,right)))

# part 2

# shorter
print(sum(left_el*right.count(left_el) for left_el in left))

# faster
simularity_score = 0
right_index =0
for left_el in left:
    i = 0
    while right_index < len(right):
        if left_el == right[right_index+i]:
            simularity_score += left_el
            i += 1
        elif left_el > right[right_index+i]:
            right_index += 1
        else:
            break
print(simularity_score)

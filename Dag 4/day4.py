from aoc import read_input
from itertools import product

# input
text = read_input("inputdag4")

# part 1
count1 = 0
for x,y in product(range(140),repeat=2):
    for i,j in product((-1,0,1),repeat = 2):
        if (x+3*i)>=0 and (x+3*i)<140 and (y+3*j)>=0 and (y+3*j)<140:
            if text[x][y] + text[x+i][y+j] + text[x+2*i][y+2*j] + text[x+3*i][y+3*j] == "XMAS":
                count1 += 1
print(count1)

# part 2
count2 = 0
match =("MS","SM")
for x,y in product(range(1,139),repeat = 2):
    if text[x][y] == 'A':
        if (text[x-1][y-1]+text[x+1][y+1] in match and text[x-1][y+1]+text[x+1][y-1] in match):
            count2+=1
print(count2)
from aoc import read_input
import re

# input
text = ''.join(read_input("inputdag3"))

# part 1
matches_part1=re.findall("mul\((\d+,\d+)\)", text)
print(sum(int(x)*int(y) for x,y in (match.split(',') for match in matches_part1)))

# part 2
matches_part2 =[]
take = True
for i in range(len(text)):
    if text[i:].startswith("do()"):
        take = True
    elif text[i:].startswith("don't()"):
        take = False
    else:
        match = re.match("mul\((\d+,\d+)\)", text[i:])
        if match and take:
            matches_part2.append(match[1])
print(sum(int(x)*int(y) for x,y in (match.split(',') for match in matches_part2)))

            
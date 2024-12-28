from aoc import read_input
from collections import OrderedDict

# input
lines = read_input("inputdag19")

# part 1
possible_towels = [towel.strip() for towel in lines[0].split(',')]
combos = lines[2:]

def towelie(combo,part2):
    possible_steps = OrderedDict()
    possible_steps[""] = 1
    total = 0
    while possible_steps:
        step,aantal = possible_steps.popitem(False)

        if step == combo:
            if part2:
                total += aantal
            else:
                return True
            
        for towel in possible_towels:
            if combo.startswith(step+towel):
                if step+towel in possible_steps:
                    possible_steps[step+towel] += aantal
                else:
                    possible_steps[step+towel] = aantal
        
    return total if part2 else False


print(sum(towelie(combo,False) for combo in combos))

# part 2
print(sum(towelie(combo,True) for combo in combos))









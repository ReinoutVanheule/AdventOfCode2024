from aoc import read_input
from operator import add, mul

# input
lines = read_input("inputdag7")
lines = dict([line.split(": ") for line in lines])
lines = {int(key):[int(v) for v in value.split()] for key,value in lines.items()}

pipe = lambda a,b: int(str(a)+str(b))
operators = [add,mul,pipe]
def operate(value_to_reach, current_value, remaining, part2 = False):
    if remaining:
        for operator in operators[:3 if part2 else 2]:
            if operate(value_to_reach, operator(current_value,remaining[0]),remaining[1:],part2):
                return True
    else:
        return current_value == value_to_reach
    
# part 1
print(sum(k for k,v in lines.items() if operate(k,v[0],v[1:])))

# part 2
print(sum(k for k,v in lines.items() if operate(k,v[0],v[1:],True)))

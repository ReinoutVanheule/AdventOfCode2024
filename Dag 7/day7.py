from aoc import read_input

# input
lines = read_input("inputdag7")

lines = dict([line.split(": ") for line in lines])
lines = {int(key):[int(v) for v in value.split()] for key,value in lines.items()}

def operate(value_to_reach, current_value, remaining, part2 = False):
    if remaining:
        status_add = operate(value_to_reach, current_value + remaining[0],remaining[1:],part2)
        status_multiply = operate(value_to_reach, current_value * remaining[0],remaining[1:],part2)
        status_pipe = operate(value_to_reach, int(str(current_value)+str(remaining[0])), remaining[1:],part2)
        return status_add or status_multiply or status_pipe and part2
    else:
        return current_value == value_to_reach
    
# part 1
print(sum(k for k,v in lines.items() if operate(k,v[0],v[1:])))

# part 2
print(sum(k for k,v in lines.items() if operate(k,v[0],v[1:],True)))

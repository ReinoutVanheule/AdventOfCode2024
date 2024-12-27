# input
program_str = "2,4,1,1,7,5,1,4,0,3,4,5,5,5,3,0,"
program = list(map(int,program_str[:-1].split(',')))

# part 1
def run_program(a,program):
    register = {'A':a,'B':0,'C':0}
    combo = lambda x: x if x <=3 else register['A'] if x == 4 else register['B'] if x== 5 else register['C']
    output = ""
    index = 0
    while index < len(program):
        opcode = program[index]
        operand = program[index+1]
        new_index = index+2      
        if opcode == 0:
            register['A'] >>= combo(operand)
        elif opcode == 1:
            register['B'] ^= operand
        elif opcode == 2:
            register['B'] = combo(operand)%8
        elif opcode == 3:
            if register['A'] != 0:
                new_index = operand
        elif opcode == 4:
            register['B'] ^= register['C']
        elif opcode == 5:
            output += str(combo(operand)%8)+','
        elif opcode == 6:
            register['B'] = register['A']>>combo(operand)
        elif opcode == 7:
            register['C'] = register['A']>>combo(operand)
        index = new_index
    return output
print(run_program(65804993,program))

# part 2
concat = ["001","010","011","000","100","101","110","111"]
existing_combos= [""]
for i in range(len(program)):
    new_combos = []
    for current_a in existing_combos:
        for cc in concat:
            a  = current_a +cc
            output = run_program(int(a,2),program)
            if program_str[30-2*i:].startswith(output):
                new_combos.append(a)
    existing_combos = new_combos

print(min(int(i,2) for i in existing_combos))

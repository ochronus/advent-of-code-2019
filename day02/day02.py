import copy

with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')

instructions = [int(x) for x in data.split(',')]

def simulate(noun, verb, orig_instructions):
    instructions = copy.copy(orig_instructions)
    instructions[1] = noun
    instructions[2] = verb

    cur_i = None
    ip = 0
    while cur_i != 99:
        cur_i = instructions[ip]
        if cur_i == 99:
            break
        if cur_i != 1 and cur_i != 2:
            print("I'm at ", ip, "and encountered a wrong instruction: ", cur_i)
            
        pos1 = instructions[ip+1]
        pos2 = instructions[ip+2]
        res_pos = instructions[ip+3]

        if cur_i == 1:
            instructions[res_pos] = instructions[pos1] + instructions[pos2]
        if cur_i == 2:
            instructions[res_pos] = instructions[pos1] * instructions[pos2]

        ip += 4

    return(instructions[0])

print(simulate(12, 2, instructions))
noun = 0
verb = 0
for noun in range(100):
    for verb in range(100):
        if simulate(noun, verb, instructions) == 19690720:
            print(noun * 100 + verb)
            break


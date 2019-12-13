# *SIGH* another implementation of the intcode computer
# this time with generators, just for fun. Looks simpler than queues

import collections

ARITIES = {
    99: 0,
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 1,
}

IMMEDIATE = 1
RELATIVE = 2

ADD = 1
MUL = 2
IN = 3
OUT = 4
JUMP_TRUE = 5
JUMP_FALSE = 6
LESS_THAN = 7
EQUALS = 8
ADD_RELATIVE_BASE = 9
HALT = 99


def parse_instruction(program, ip, relbase):
    instruction = program[ip]
    ip += 1
    values = []
    locations = []
    for i in range(ARITIES[instruction % 100]):
        mode = (instruction // (10 ** (2 + i))) % 10
        loc = program[ip]
        val = program[program[ip]]
        if mode == IMMEDIATE:
            loc = None
            val = program[ip]
        if mode == RELATIVE:
            loc = program[ip] + relbase
            val = program[program[ip] + relbase]
        locations.append(loc)
        values.append(val)
        ip += 1
    return(instruction % 100, values, locations, ip)


def computer(code, name=''):
    ip = 0
    outputs = []

    program = collections.defaultdict(int)
    for i, v in enumerate(code):
        program[i] = v

    relbase = 0

    while program[ip] != HALT:
        instruction, values, locations, ip = parse_instruction(program, ip, relbase)
        if instruction == ADD:
            program[locations[2]] = values[0] + values[1]
        if instruction == MUL:
            program[locations[2]] = values[0] * values[1]
        if instruction == IN:
            program[locations[0]] = yield 'input_needed'
        if instruction == OUT:
            yield values[0]
        if instruction == JUMP_TRUE:
            if values[0] != 0:
                ip = values[1]
        if instruction == JUMP_FALSE:
            if values[0] == 0:
                ip = values[1]
        if instruction == LESS_THAN:
            program[locations[2]] = int(values[0] < values[1])
        if instruction == EQUALS:
            program[locations[2]] = int(values[0] == values[1])
        if instruction == ADD_RELATIVE_BASE:
            relbase += values[0]

    return program[0], outputs[0] if outputs else None

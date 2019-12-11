POSITION = 0
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

READ = 0
WRITE = 1

INSTRUCTION_ARGS = {
    ADD: (READ, READ, WRITE),
    MUL: (READ, READ, WRITE),
    IN: (WRITE,),
    OUT: (READ,),
    JUMP_TRUE: (READ, READ),
    JUMP_FALSE: (READ, READ),
    LESS_THAN: (READ, READ, WRITE),
    EQUALS: (READ, READ, WRITE),
    ADD_RELATIVE_BASE: (READ,),
    HALT: (),
}


class Computer:
    def __init__(self, code, inp):
        self.code = list(code)
        self.inp = inp

    def __getitem__(self, index):
        return self.mem[index]

    def __setitem__(self, index, val):
        self.mem[index] = val

    def get_args(self, arg_kinds, modes):
        args = [None] * 4

        for i, kind in enumerate(arg_kinds):
            a = self[self.ip + 1 + i]
            mode = modes % 10
            modes //= 10

            if mode == RELATIVE:
                a += self.relative_base

            if mode in (POSITION, RELATIVE):
                if a >= len(self.mem):
                    self.mem += [0] * (a + 1 - len(self.mem))

                if kind == READ:
                    a = self[a]

            args[i] = a

        return args

    def run(self):
        self.ip = 0
        self.relative_base = 0
        self.mem = self.code.copy()
        out = None

        while self[self.ip] != HALT:
            instr = self[self.ip]
            instruction = instr % 100
            modes = instr // 100

            arg_kinds = INSTRUCTION_ARGS[instruction]
            a, b, c, _ = self.get_args(arg_kinds, modes)
            self.ip += 1 + len(arg_kinds)

            if instruction == IN:
                self[a] = self.inp
            if instruction == OUT:
                out = a
            if instruction == ADD:
                self[c] = a + b
            if instruction == MUL:
                self[c] = a * b
            if instruction == LESS_THAN:
                self[c] = 1 if a < b else 0
            if instruction == EQUALS:
                self[c] = 1 if a == b else 0
            if instruction == JUMP_TRUE:
                if a != 0:
                    self.ip = b
            if instruction == JUMP_FALSE:
                if a == 0:
                    self.ip = b
            if instruction == ADD_RELATIVE_BASE:
                self.relative_base += a

        return out

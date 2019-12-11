CODE_BUFFER = 100000

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


class OutputException(Exception):
    def __init__(self, output):
        self.output = output

class HaltException(Exception):
    pass

class Computer:
    def __init__(self, code):
        self.code = code + [0 for _ in range(CODE_BUFFER)]
        self.ip = 0
        self.relative_base = 0

    def run(self, inputs):
        while True:
            instruction = self.code[self.ip] % 100
            if instruction == HALT:
                raise HaltException()

            address_mode1 = self.code[self.ip] // 100 % 10
            address_mode2 = self.code[self.ip] // 1000 % 10
            address_mode3 = self.code[self.ip] // 10000 % 10

            if address_mode1 == RELATIVE:
                value1 = self.relative_base + self.code[self.ip+1]
            else:
                value1 = self.ip+1 if address_mode1 == IMMEDIATE else self.code[self.ip+1]

            if address_mode2 == RELATIVE:
                value2 = self.relative_base + self.code[self.ip+2]
            else:
                value2 = self.ip+2 if address_mode2 == IMMEDIATE else self.code[self.ip+2]

            if address_mode3 == RELATIVE:
                value3 = self.relative_base + self.code[self.ip+3]
            else:
                value3 = self.ip+3 if address_mode3 == IMMEDIATE else self.code[self.ip+3]

            if instruction == ADD:
                self.code[value3] = self.code[value1] + self.code[value2]
                self.ip += 4
            elif instruction == MUL:
                self.code[value3] = self.code[value1] * self.code[value2]
                self.ip += 4
            elif instruction == IN:
                self.code[value1] = inputs.pop(0)
                self.ip += 2
            elif instruction == OUT:
                output_value = self.code[value1]
                self.ip += 2
                raise OutputException(output_value)
            elif instruction == JUMP_TRUE:
                if self.code[value1] != 0:
                    self.ip = self.code[value2]
                else:
                    self.ip += 3
            elif instruction == JUMP_FALSE:
                if self.code[value1] == 0:
                    self.ip = self.code[value2]
                else:
                    self.ip += 3
            elif instruction == LESS_THAN:
                if self.code[value1] < self.code[value2]:
                    self.code[value3] = 1
                else:
                    self.code[value3] = 0
                self.ip += 4
            elif instruction == EQUALS:
                if self.code[value1] == self.code[value2]:
                    self.code[value3] = 1
                else:
                    self.code[value3] = 0
                self.ip += 4
            elif instruction == ADD_RELATIVE_BASE:
                self.relative_base += self.code[value1]
                self.ip += 2

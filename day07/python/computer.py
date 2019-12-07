from queue import SimpleQueue


IP_INCREMENTS = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}

class HaltException(Exception):
    """Thou shalt halt!"""
    pass

class Computer:
    def __init__(self, initial_program):
        self.program_state = initial_program
        self.ip = 0
        self.inputs = SimpleQueue()

    def run(self):
        while True:
            instr = str(self.program_state[self.ip])
            instruction = int(instr[-2:])
            
            if instruction == 99:
                raise HaltException

            modes = []
            for i in range(3, IP_INCREMENTS[instruction] + 2):
                if len(instr) >= i:
                    modes.append(int(instr[-i]))
                else:
                    modes.append(0)

            params = []
            for i in range(1, IP_INCREMENTS[instruction]):
                if modes[i - 1] == 0:
                    params.append(self.program_state[self.program_state[self.ip + i]])
                else:
                    params.append(self.program_state[self.ip + i])

            if instruction == 1:
                outpos = self.program_state[self.ip + 3]
                self.program_state[outpos] = params[0] + params[1]
            
            if instruction == 2:
                outpos = self.program_state[self.ip + 3]
                self.program_state[outpos] = params[0] * params[1]
            
            if instruction == 3:
                outpos = self.program_state[self.ip + 1]
                self.program_state[outpos] = self.inputs.get()
            
            if instruction == 4:
                self.ip += 2
                return params[0]
            
            if instruction == 5:
                if params[0] != 0:
                    self.ip = params[1]
                    continue
            
            if instruction == 6:
                if params[0] == 0:
                    self.ip = params[1]
                    continue
            
            if instruction == 7:
                outpos = self.program_state[self.ip + 3]
                if params[0] < params[1]:
                    self.program_state[outpos] = 1
                else:
                    self.program_state[outpos] = 0
            
            if instruction == 8:
                outpos = self.program_state[self.ip + 3]
                if params[0] == params[1]:
                    self.program_state[outpos] = 1
                else:
                    self.program_state[outpos] = 0

            self.ip += IP_INCREMENTS[instruction]

    def give_signal(self, obj):
        self.inputs.put(obj)

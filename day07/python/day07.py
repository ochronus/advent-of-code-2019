from itertools import permutations
from queue import SimpleQueue
from computer import Computer, HaltException


def part1(program):
    phase_settings = permutations(range(5))
    highest_output_signal = 0
    for phase_setting in phase_settings:
        amplifiers = []
        for i in range(5):
            amplifiers.append(Computer(program))
            amplifiers[i].give_signal(phase_setting[i])

        signal = 0
        for i in range(5):
            amplifiers[i].give_signal(signal)
            signal = amplifiers[i].run()
        highest_output_signal = max(highest_output_signal, signal)
    return(highest_output_signal)

def part2(program):
    phase_settings = permutations(range(5, 10))
    highest_output_signal = 0
    for phase_setting in phase_settings:
        amplifiers = []
        for i in range(5):
            amplifiers.append(Computer(program))
            amplifiers[i].give_signal(phase_setting[i])

        signal = 0
        should_halt = False
        while not should_halt:
            for i in range(5):
                amplifiers[i].give_signal(signal)
                try:
                    signal = amplifiers[i].run()
                except HaltException:
                    should_halt = True
        highest_output_signal = max(highest_output_signal, signal)
    return(highest_output_signal)


with open("../input.txt") as f:
    acs = list([int(i) for i in f.read().split(",")])

print(part1(acs))
print(part2(acs))

from computer import Computer


with open("../input.txt") as f:
    code = list(map(int, f.readline().strip().split(",")))

    print("Part 1:", Computer(code, 1).run())
    print("Part 2:", Computer(code, 2).run())

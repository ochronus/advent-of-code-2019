def mass2fuel(mass):
    return mass // 3 - 2

def part1(data):
    return sum(mass2fuel(datum) for datum in data)


def fuels(mass):
    while (mass := mass2fuel(mass)) > 0:
        yield mass

def part2(data):
    return sum(mass for datum in data for mass in fuels(datum))


with open("input.txt") as f:
    data = [int(l) for l in f.read().splitlines()]

print(part1(data))
print(part2(data))
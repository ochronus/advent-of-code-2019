import collections
import math
import re


def step(moons):
    moons_next_state = moons
    for i, moon in enumerate(moons):                    # set velocities
        for j, moon2 in enumerate(moons):
            if i >= j:
                continue
            for axis in (0, 1, 2):
                if moon[axis] < moon2[axis]:
                    moons_next_state[i][axis+3] += 1
                    moons_next_state[j][axis+3] -= 1
                elif moon[axis] > moon2[axis]:
                    moons_next_state[i][axis+3] -= 1
                    moons_next_state[j][axis+3] += 1
    for moon in moons_next_state:                       # apply velocities
        moon[0] += moon[3]
        moon[1] += moon[4]
        moon[2] += moon[5]
    return moons_next_state


def lcm(a, b):
    return a // math.gcd(a, b) * b


def calc_energy(moon):
    px, py, pz, vx, vy, vz = moon
    return(abs(px) + abs(py) + abs(pz)) * (abs(vx) + abs(vy) + abs(vz))


def get_indices(axis):
    if axis == 'x':
        return(0, 3)
    if axis == 'y':
        return(1, 4)
    if axis == 'z':
        return(2, 5)


def check_axis(moons, axis, seen):
    index1, index2 = get_indices(axis)
    pos_vel = str([[m[index1], m[index2]] for m in moons])
    if pos_vel in seen:
        return True
    else:
        seen.add(pos_vel)
        return False


with open("../input.txt") as f:
    lines = [[int(i) for i in re.findall(r'-?\d+', l.strip())] for l in f.readlines()]
initial_moon_state = [line + [0,0,0] for line in lines]         # positions plus initial velocities
moons = initial_moon_state.copy()
for i in range(1000):
    moons = step(moons)
energies = [calc_energy(moon) for moon in moons]
print("Part 1:", sum(energies))


moons = initial_moon_state.copy()
seen_x_axis = seen_y_axis = seen_z_axis = set()
x_axis_repeated_at = y_axis_repeated_at = z_axis_repeated_at = None

for i in range(300000):                                     # had to experiment to get it high enough
    if x_axis_repeated_at and y_axis_repeated_at and z_axis_repeated_at:    # we've found our first repetition of the whole alignment
        break
    moons = step(moons)
    if not x_axis_repeated_at:
        if check_axis(moons, 'x', seen_x_axis):
            x_axis_repeated_at = i
    if not y_axis_repeated_at:
        if check_axis(moons, 'y', seen_y_axis):
            y_axis_repeated_at = i
    if not z_axis_repeated_at:
        if check_axis(moons, 'z', seen_z_axis):
            z_axis_repeated_at = i


print("Part 2:", lcm(lcm(x_axis_repeated_at, y_axis_repeated_at), z_axis_repeated_at))

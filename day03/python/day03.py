WIRE1, WIRE2 = [wire.split(',') for wire in open('../input.txt').read().split()]


def follow_wire(wire):
    points = {}
    x = 0
    y = 0
    length = 0

    for step in wire:
        direction = step[0]
        step_count = int(step[1:])
        for _ in range(step_count):
            length += 1
            x += 0 if direction in ['U', 'D'] else (1 if direction == 'R' else -1)
            y += 0 if direction in ['L', 'R'] else (1 if direction == 'U' else -1)

            if (x, y) not in points:
                points[(x, y)] = length
    
    return points


wire1_points = follow_wire(WIRE1)
wire2_points = follow_wire(WIRE2)
crossings = set(wire1_points.keys()) & set(wire2_points.keys())

part1 = min([(abs(x) + abs(y)) for (x, y) in crossings])
part2 = min([(wire1_points[point] + wire2_points[point]) for point in crossings])

print(part1)
print(part2)
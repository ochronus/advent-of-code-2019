from computer import Computer, HaltException, OutputException


DIRECTIONS = {
    0: (0,1),
    1: (1,0),
    2: (0,-1),
    3: (-1,0),
    }

OUTPUT_PAINT = 0
OUTPUT_TURN = 1


def turtle_paint(code, color):
    grid = {}
    computer = Computer(code.copy())
    robot_position = (0,0)
    robot_direction = 0
    color = color
    output_type = OUTPUT_PAINT

    while True:
        try:
            if output_type == OUTPUT_PAINT:
                computer.run([color])
            else:
                computer.run([])
        except OutputException as e:
            if output_type == OUTPUT_PAINT:
                grid[robot_position] = e.output
                output_type = OUTPUT_TURN
            elif output_type == OUTPUT_TURN:
                if e.output == 0:
                    robot_direction = (robot_direction - 1) % 4
                if e.output == 1:
                    robot_direction = (robot_direction + 1) % 4
                robot_position = (robot_position[0] + DIRECTIONS[robot_direction][0], robot_position[1] + DIRECTIONS[robot_direction][1])
                if robot_position in grid:
                    color = grid[robot_position]
                else:
                    color = 0
                output_type = OUTPUT_PAINT
        except HaltException:
            break
    return(grid)

def part1(code):
    grid = turtle_paint(code, 0)
    return len(grid.keys())


def part2(code):
    grid = turtle_paint(code, 1)
    minx = maxx = miny = maxy = 0
    for point in grid:
        if point[0] < minx:
            minx = point[0]
        if point[0] > maxx:
            maxx = point[0]
        if point[1] < miny:
            miny = point[1]
        if point[1] > maxy:
            maxy = point[1]
    width = maxx - minx + 1
    height = maxy - miny + 1
    license_plate = [[' ' for _ in range(width)] for _ in range(height)]
    for point in grid:
        license_plate[point[1] - miny][point[0] - minx] = ' █'[grid[point]]

    license_plate.reverse()
    lines = []
    for row in license_plate:
        lines.append(''.join(row))
    
    return "\n".join(lines)
    
code = [int(x) for x in open("../input.txt").read().strip().split(",")]
print("Part 1:", part1(code))
print("Part 2:")
print(part2(code))
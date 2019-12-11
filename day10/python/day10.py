import math

grid = [line.strip() for line in open("../input.txt").readlines()]

height = len(grid)
width = len(grid[0])

def gcd(x, y):
    return y if x == 0 else gcd(y % x, x)


winner_asteroid = (0, 0, 0, set())
for y in range(height):
    for x in range(width):
        if grid[y][x] != '#':
            continue
        seen = set()
        for y2 in range(height):
            for x2 in range(width):
                if grid[y2][x2] != '#':
                    continue
                if y2 == y and x2 ==x:
                    continue
                dy = y2 - y
                dx = x2 - x
                scaledown = abs(gcd(dy, dx))
                # nearest possible point in line of sight
                nearest_in_line_y = -dy // scaledown
                nearest_in_line_x = dx // scaledown
                seen.add((nearest_in_line_y, nearest_in_line_x))
        if len(seen) > winner_asteroid[0]:
            winner_asteroid = (len(seen), y, x, seen)

count, station_y, station_x, seen = winner_asteroid
print("Part 1:", count)


# len(seen) > 200 so one swipe is enough
angles = []
for (dy, dx) in seen:
    angle = math.atan2(dy, dx)
    if angle > math.pi/2.0:
        angle -= 2*math.pi
    angles.append((angle, (dy, dx)))
angles = sorted(angles, reverse=True)

asteroid_no_200 = angles[199][1]
asteroid_y = station_y - asteroid_no_200[0]
asteroid_x = station_x + asteroid_no_200[1]

# since we only have the line of sight defined at this point, let's find the first asteroid on it
while grid[asteroid_y][asteroid_x] != '#':
    asteroid_y -= asteroid_no_200[0]
    asteroid_x += asteroid_no_200[1]

print("Part 2:", asteroid_x*100+asteroid_y)

from computer import computer


BLOCK_TILE = 2
HORIZONTAL_PADDLE = 3
BALL_TILE = 4
PLAY_FOR_FREE = 2

code = [int(x) for x in open("../input.txt").read().strip().split(",")]

grid = {}
comp = computer(code)

try:
    while True:
        x, y, tile_or_score = next(comp), next(comp), next(comp)
        grid[x, y] = tile_or_score
except StopIteration:
    pass

print(len([tile_or_score for _, tile_or_score in grid.items() if tile_or_score == BLOCK_TILE]))

code[0] = PLAY_FOR_FREE
comp = computer(code)
ball_x = 0
pad_x = 0
score = 0
try:
    while True:
        x = next(comp)
        while x == 'input_needed':
            if ball_x > pad_x:
                joystick_input = 1
            if ball_x == pad_x:
                joystick_input = 0
            if ball_x < pad_x:
                joystick_input = -1    
            x = comp.send(joystick_input)
        y = next(comp)
        tile_or_score = next(comp)
        if (x, y) == (-1, 0):
            score = tile_or_score
        if tile_or_score == HORIZONTAL_PADDLE:
            pad_x = x
        if tile_or_score == BALL_TILE:
            ball_x = x
except StopIteration:
    pass

print(score)


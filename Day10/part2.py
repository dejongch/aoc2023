from enum import Enum
from pprint import pprint

class directions(Enum):
    up = 0
    down = 1
    left = 2
    right = 3

transforms = {
    directions.up: (0, -1, directions.up),
    directions.down: (0, 1, directions.down),
    directions.left: (-1, 0, directions.left),
    directions.right: (1, 0, directions.right)
}

pipe_types = {
    "|": {
        directions.up: directions.up,
        directions.down: directions.down
    },
    "-": {
        directions.right: directions.right,
        directions.left: directions.left
    },
    "L": {
        directions.down: directions.right,
        directions.left: directions.up,
    },
    "J": {
        directions.down: directions.left,
        directions.right: directions.up
    },
    "7": {
        directions.right: directions.down,
        directions.up: directions.left
    },
    "F": {
        directions.left: directions.down,
        directions.up: directions.right
    }
}

maps = []
start = None

with open("input.txt", 'r') as file:
    for index, line in enumerate(file):
        if not start and "S" in line:
            start = (line.index("S"), index)
        maps.append(line.strip())
        
loop_extended = [[0 for _ in range(len(line)*2)] for _ in range(len(maps)*2)]


def move_pipe(current_location, direction, update_loop=True):
    current_x = current_location[0]
    current_y = current_location[1]
    transform_x = transforms[direction][0]
    transform_y = transforms[direction][1]

    if update_loop:
        loop_extended[(current_y * 2)][(current_x * 2)] = 1
        loop_extended[current_y * 2 + transform_y][current_x * 2 + transform_x] = 1

    return (
        current_x + transform_x,
        current_y + transform_y,
        transforms[direction][2]
    )

def move_from_location(location):
    return move_pipe(
        location,
        pipe_types[get_pipe_value(location)][location[2]]
    )

def get_pipe_value(location):
    return maps[location[1]][location[0]]

loop_extended[(start[1]*2)][(start[0]*2)] = 1

current_locations = []
for direction in directions:
    new_location = move_pipe(start, direction, False)
    if pipe_types.get(get_pipe_value(new_location), {}).get(direction):
        current_locations.append(new_location)
        move_pipe(start, direction)




steps = 1
while (
    current_locations[0][0] != current_locations[1][0]
    or current_locations[0][1] != current_locations[1][1]
):
    current_locations[0] = move_from_location(current_locations[0])
    current_locations[1] = move_from_location(current_locations[1])
    steps += 1
current_locations[0] = move_from_location(current_locations[0])

print(steps)

def count_encased_zeros_even_positions(grid):
    rows, cols = len(grid), len(grid[0]) if grid else 0

    def is_on_edge(r, c):
        return r == 0 or r == rows - 1 or c == 0 or c == cols - 1

    def dfs_iterative(r, c):
        if grid[r][c] != 0:
            return 0

        stack = [(r, c)]

        while stack:
            x, y = stack.pop()
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != 0:
                continue

            grid[x][y] = 2  # Mark as visited

            # Add adjacent cells to the stack
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                stack.append((x + dx, y + dy))

    def flood_fill_edge_zeros():
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and is_on_edge(r, c):
                    dfs_iterative(r, c)  # Flood fill all edge zeros to -1

    flood_fill_edge_zeros()
    encased_zeros_even_positions = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and r%2 == 0 and c%2==0:
                encased_zeros_even_positions += 1

    return encased_zeros_even_positions

print(count_encased_zeros_even_positions(loop_extended))
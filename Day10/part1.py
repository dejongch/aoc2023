from enum import Enum

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
        



def move_pipe(current_location, direction):
    return (
        current_location[0] + transforms[direction][0],
        current_location[1] + transforms[direction][1],
        transforms[direction][2]
    )

def move_from_location(location):
    return move_pipe(
        location,
        pipe_types[get_pipe_value(location)][location[2]]
    )

def get_pipe_value(location):
    return maps[location[1]][location[0]]


current_locations = []
for direction in directions:
    new_location = move_pipe(start, direction)
    if pipe_types.get(get_pipe_value(new_location), {}).get(direction):
        current_locations.append(new_location)

steps = 1
while (
    current_locations[0][0] != current_locations[1][0]
    or current_locations[0][1] != current_locations[1][1]
):
    current_locations[0] = move_from_location(current_locations[0])
    current_locations[1] = move_from_location(current_locations[1])
    steps += 1

print(steps)

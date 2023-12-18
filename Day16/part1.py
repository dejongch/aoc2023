from enum import Enum, auto

class Direction(Enum):
    north = auto()
    east = auto()
    south = auto()
    west = auto()

transforms = {
    Direction.north: (0, -1),
    Direction.south: (0, 1),
    Direction.west: (-1, 0),
    Direction.east: (1, 0)
}

space_input_outputs = {
    ".":{
        Direction.north: [Direction.north],
        Direction.east: [Direction.east],
        Direction.south: [Direction.south],
        Direction.west: [Direction.west],
    },
    "\\":{
        Direction.north: [Direction.west],
        Direction.east: [Direction.south],
        Direction.south: [Direction.east],
        Direction.west: [Direction.north],
    },
    "/": {
        Direction.north: [Direction.east],
        Direction.east: [Direction.north],
        Direction.south: [Direction.west],
        Direction.west: [Direction.south],
    },
    "|": {
        Direction.north: [Direction.north],
        Direction.east: [Direction.north, Direction.south],
        Direction.south: [Direction.south],
        Direction.west: [Direction.north, Direction.south],
    },
    "-": {
        Direction.north: [Direction.east, Direction.west],
        Direction.east: [Direction.east],
        Direction.south: [Direction.east, Direction.west],
        Direction.west: [Direction.west],
    }
}

map = []
with open("input.txt", 'r') as file:
    for line in file:
        map.append(line.strip())

previous_beam_tips = {
    (0,0): {
        Direction.east: True
    }
}

map_width = len(map[0])
map_height = len(map)

def get_space(beam_tip):
    return map[beam_tip[0][1]][beam_tip[0][0]]

def get_new_location(beam_tip, direction):
    transform = transforms[direction]
    new_x = beam_tip[0][0] + transform[0]
    new_y = beam_tip[0][1] + transform[1]

    return (new_x, new_y)

def move_beam(initial_beam_tip):
    # Initialize the stack with the initial beam tip
    stack = [initial_beam_tip]

    while stack:
        # Pop the last element from the stack
        beam_tip = stack.pop()
        current_space = get_space(beam_tip)
        new_directions = space_input_outputs[current_space][beam_tip[1]]

        for direction in new_directions:
            new_location = get_new_location(beam_tip, direction)

            # Check for valid location and unvisited state
            if (0 <= new_location[0] < map_width and
                0 <= new_location[1] < map_height and
                previous_beam_tips.get(new_location, {}).get(direction) is None):
                
                # Mark this location and direction as visited
                previous_beam_tips.setdefault(new_location, {})[direction] = True

                # Add the new beam tip to the stack for further processing
                stack.append((new_location, direction))

        # The loop continues until the stack is empty

move_beam(((0, 0), Direction.east))

print(len(previous_beam_tips.keys()))
            



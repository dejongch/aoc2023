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

previous_beam_tips = {}

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
    initial_location = initial_beam_tip[0]
    initial_direction = initial_beam_tip[1]
    
    spaces_hit = set()
    callback_stack = []

    def initial_callback(paths_hits):
        previous_beam_tips.setdefault(initial_location, {}).setdefault(initial_direction, [])
        
        previous_beam_tips[initial_location][initial_direction] += paths_hits
        spaces_hit.update(previous_beam_tips[initial_location][initial_direction])

    stack = [(initial_beam_tip, initial_callback)]

    while stack:
        beam_tip, completion_callback = stack.pop()
        current_space = get_space(beam_tip)
        new_directions = space_input_outputs[current_space][beam_tip[1]]

        for direction in new_directions:
            new_location = get_new_location(beam_tip, direction)

            if (0 <= new_location[0] < map_width and
                0 <= new_location[1] < map_height and
                previous_beam_tips.get(new_location, {}).get(direction) is None):

                previous_beam_tips.setdefault(new_location, {})[direction] = []

                def callback(paths_hit, callback_location=new_location, callback_direction=direction):
                    if(paths_hit):
                        previous_beam_tips[callback_location][callback_direction] += paths_hit
                        spaces_hit.update(previous_beam_tips[callback_location][callback_direction])
                        callback_stack.append((previous_beam_tips[callback_location][callback_direction], completion_callback))

                stack.append(((new_location, direction), callback))
            else:
                callback_stack.append(([beam_tip[0]], completion_callback))

        # Process callbacks iteratively
        while callback_stack:
            paths_hit, callback = callback_stack.pop()
            callback(paths_hit)

    return len(spaces_hit)

most_energized = 0

for x in range(map_height):
    most_energized = max(
        most_energized, 
        move_beam(((0, x), Direction.east)),
        move_beam(((0, map_height - x - 1), Direction.west)),
        move_beam(((x, 0), Direction.south)),
        move_beam(((map_height - x - 1, 0), Direction.north)))

print(most_energized)
            



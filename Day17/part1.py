import heapq
from enum import IntEnum

class Directions(IntEnum):
    north = -1
    east = 2
    south = 1
    west = -2

transforms = {
    Directions.north: (0, -1),
    Directions.south: (0, 1),
    Directions.west: (-1, 0),
    Directions.east: (1, 0)
}

map = []

with open("input.txt", 'r') as file:
    for line in file:
        map.append([int(item) for item in line.strip()])

def find_path(map):
    start = (0,0)
    rows = len(map)
    columns = len(map[0])
    end = (columns-1, rows -1)

    def heuristic(location):
        return (end[0] - location[0]) + (end[1] - location[1])
    
    def heat_loss(location):
        return map[location[1]][location[0]]
    
    def get_new_location(location, direction):
        transform = transforms[direction]
        new_location = (location[0] + transform[0], location[1] + transform[1])
        if (
                0 <= new_location[0] < columns
                and 0 <= new_location[1] < rows
        ):
            return new_location
        return None
    
    open_set = []
    open_set_dict = {}
    heapq.heappush(open_set, (0 + heuristic(start), 0, start, Directions.east, 0))
    open_set_dict[(start, Directions.east, 0)] = 0
    visited_states = set()

    while open_set:
        _, heat_lost, location, direction, repeated_direction_count = heapq.heappop(open_set)

        if location[0] == end[0] and location[1] == end[1]:
            return heat_lost
        
        visited_states.add((location, direction, repeated_direction_count))
        del open_set_dict[(location, direction, repeated_direction_count)]
        new_directions = [(Directions.east, 1), (Directions.south, 1)]
        if direction:
            new_directions = [(3-abs(direction), 1)]
            new_directions.append((new_directions[0][0]*-1, 1))

            if repeated_direction_count < 3:
                new_directions.append((direction, repeated_direction_count+1))

        for new_direction, new_repeated_direction_count in new_directions:
            if (
                (new_location := get_new_location(location, new_direction))
                and (new_location, new_direction, new_repeated_direction_count) not in visited_states
            ):
                new_heat_loss = heat_lost + heat_loss(new_location)
                if (
                    (previous_hit:=open_set_dict.get((new_location, new_direction, new_repeated_direction_count))) is None
                    or previous_hit > new_heat_loss
                ):
                    heapq.heappush(open_set, (new_heat_loss + heuristic(new_location), new_heat_loss, new_location, new_direction, new_repeated_direction_count))
                    open_set_dict[(new_location, new_direction, new_repeated_direction_count)] = new_heat_loss
    
    return float('inf')

heat_loss = find_path(map)
print(heat_loss)

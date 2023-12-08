from collections import defaultdict

with open("input.txt", 'r') as file:
    locations = {
        0: (0,0),
        1: (0,0)
    }
    locations_visit_count: dict[tuple[int,int], int] = defaultdict(int, {(0,0): 2})

    x_change = {
        ">": 1,
        "<": -1,
        "v": 0,
        "^": 0
    }
    y_change = {
        ">": 0,
        "<": 0,
        "v": 1,
        "^": -1
    }
    for line in file:
        for index, direction in enumerate(line):
            current_location = locations[index%2]
            current_x, current_y = current_location
            locations[index%2] = (current_x + x_change[direction], current_y + y_change[direction])
            locations_visit_count[locations[index%2]] += 1
    print(len(locations_visit_count))
from collections import defaultdict

with open("input.txt", 'r') as file:
    current_location: tuple[int, int] = (0,0)
    locations_visit_count: dict[tuple[int,int], int] = defaultdict(int, {(0,0): 1})

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
            current_x, current_y = current_location
            current_location = (current_x + x_change[direction], current_y + y_change[direction])
            locations_visit_count[current_location] += 1
    print(len(locations_visit_count))

from concurrent.futures.process import _threads_wakeups
import re
from readline import set_completion_display_matches_hook

regex = r"(.) (\d\d?) \((.*)\)"

current_location = (0,0)

dug_locations = {
    current_location: True
}

transforms = {
    "U": (0, -1),
    "D": (0, 1),
    "R": (1, 0),
    "L": (-1, 0)
}
with open("input.txt", 'r') as file:
    for direction, distance, colour in [re.match(regex, line.strip()).groups() for line in file]:
        distance = int(distance)
        transform = transforms[direction]
        for _ in range(distance):
            current_location = (current_location[0] + transform[0], current_location[1] + transform[1])
            dug_locations[current_location] = True


total = len(dug_locations)
sorted_dug_locations = sorted(dug_locations.keys(), key=lambda x: (x[1], x[0]))
top_left_point = sorted_dug_locations[0]
min_y = top_left_point[1]
max_y = sorted_dug_locations[-1][1]

xs = sorted([location[0] for location in sorted_dug_locations])
min_x = xs[0]
max_x = xs[1]


searching_location = (top_left_point[0] + 1, top_left_point[1] + 1)
while dug_locations.get(searching_location):
    searching_location = (searching_location[0] + 1, searching_location[1] + 1)

def flood_fill(searching_location):
    while True:
        stack = [searching_location]
        searched = {
            searching_location: True
        }
        flood_total = 0
        while stack:
            location = stack.pop()
            flood_total+=1
            for transform in transforms.values():
                new_location = (location[0] + transform[0], location[1] + transform[1])
                if min_x > new_location[0] > max_x or min_y > new_location[1] > max_y:
                    searching_location = (searching_location[0] + 1, searching_location[1] + 1)
                    break
                if not dug_locations.get(new_location) and not searched.get(new_location):
                    stack.append(new_location)
                    searched[new_location] = True
        return flood_total
        

print(total + flood_fill(searching_location))
""" sorted_dug = sorted(dug_locations, key=lambda x: (x[1], x[0]))

current_row = sorted_dug[0][1]
current_column = sorted_dug[0][0]
in_hole = False

for location in sorted_dug[1:]:
    if current_row == location[1] and location[0] - current_column > 1:
        if in_hole:
            total += location[0] - current_column - 1
            in_hole = False
        else:
            in_hole = True
    else:
        in_hole = True
    current_column = location[0]
    current_row = location[1] """


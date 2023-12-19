from concurrent.futures.process import _threads_wakeups
import re
from readline import set_completion_display_matches_hook

regex = r".*\(#(.....)(.)\)"

current_location = (0,0)

verticies = [current_location]

transforms = {
    "3": (0, -1),
    "1": (0, 1),
    "0": (1, 0),
    "2": (-1, 0)
}

total_area = 0


with open("input.txt", 'r') as file:
    for distance, direction in [re.match(regex, line.strip()).groups() for line in file]:
        distance = int(distance, 16)
        transform = transforms[direction]
        current_location = (current_location[0] + transform[0] * distance, current_location[1] + transform[1] * distance)
        verticies.append(current_location)
        total_area += distance

total_area = total_area / 2 + 1

def shoelace_formula(vertices):
    """
    Calculate the area of a polygon using the Shoelace Formula.

    :param vertices: A list of (x, y) tuples representing the vertices of the polygon.
    :return: The area of the polygon.
    """
    n = len(vertices)  # Number of vertices
    area = 0

    # Sum over each pair of vertices
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Next vertex, with wrapping
        area += x1 * y2 - y1 * x2

    return abs(area) / 2

total_area += shoelace_formula(verticies)

print(total_area)
import math
y_position_addition = []
x_position_addition = []

non_empty_columns = {}

galaxies = []

with open("input.txt", 'r') as file:
    blank_rows = 0
    for y_index, line in enumerate(file):
        y_position_addition.append(blank_rows+y_index)
        blank_row = True
        for x_index, char in enumerate(line):
            if char == "#":
                blank_row = False
                non_empty_columns[x_index] = True
                galaxies.append((x_index, y_index))
        if blank_row:
            blank_rows+=999999
    blank_columns = 0
    for x_index in range(len(line)):
        x_position_addition.append(blank_columns+x_index)
        if not non_empty_columns.get(x_index):
            blank_columns+=999999

total_distance = 0
for a in range(len(galaxies)):
    galaxy_a = galaxies[a]
    for b in range(a+1, len(galaxies)):
        galaxy_b = galaxies[b]
        total_distance += abs(x_position_addition[galaxy_a[0]]-x_position_addition[galaxy_b[0]])
        total_distance += abs(y_position_addition[galaxy_a[1]]-y_position_addition[galaxy_b[1]]) 

print(total_distance)
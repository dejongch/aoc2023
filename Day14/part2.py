from functools import cache
from pprint import pprint
current_map = []
hash_indexes = []
with open("input.txt", 'r') as file:
    for line in file:
        row = line.strip()
        current_map.append(row)
        hash_indexes.append(tuple([index for index, value in enumerate(row) if value == "#"]))
    current_map = tuple(current_map)
    hash_indexes = tuple(hash_indexes)

size = len(current_map)

@cache
def rotate_map_clockwise(map):
    return tuple(["".join(tup) for tup in zip(*map)])

@cache
def rotate_map_counterclockwise(map):
    reversed_map = [row[::-1] for row in map]
    return tuple("".join(tup) for tup in zip(*reversed_map))


@cache
def tilt_row(row):
    size = len(row)
    hash_index = [-1] + [index for index, value in enumerate(row) if value == "#"] + [size]
    round_groups_size = [len(group) for group in row.replace(".", "").split("#")]
    new_group_strings = []
    for index, size in enumerate(round_groups_size):
        division_size = hash_index[index + 1] - hash_index[index]
        num_of_empty = division_size - size - 1
        new_group_strings.append(f"{'O'*size}{'.'*num_of_empty}")
    return "#".join(new_group_strings)


@cache
def tilt_map(rotated_map):
    new_map = []
    for row in rotated_map:
        new_map.append(tilt_row(row))
    return tuple(new_map)

@cache
def cycle_map(map):
    map = rotate_map_clockwise(map)
    for _ in range(4):
        map = tilt_map(map)
        map = rotate_map_counterclockwise(map)
    return rotate_map_clockwise(map)

map_steps = {}
maps = []

total_steps = 1000000000
for step in range(total_steps):
    current_map = cycle_map(current_map)
    if map_step:=map_steps.get(current_map):
        print(step)
        print(map_step)
        final_step_equivilant = (total_steps-1 - map_step) % (step-map_step) + map_step
        current_map = maps[final_step_equivilant]
        break
    map_steps[current_map] = step
    maps.append(current_map)
    
pprint(current_map)

weight = 0
for index in range(size):
    weight += current_map[index].count("O") * (size-index)

print(weight)

print(rotate_map_clockwise.cache_info().hits)
print(rotate_map_counterclockwise.cache_info().hits)
print(tilt_row.cache_info().hits)
print(tilt_map.cache_info().hits)
print(cycle_map.cache_info().hits)
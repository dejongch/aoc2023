def find_reflection(map):
    map_length = len(map)
    for reflection_index in range(map_length-1):
        difference = 0
        reflection_possible = True
        while reflection_possible:
            check_index = reflection_index - difference
            opposite_index = reflection_index + 1 + difference
            
            if check_index < 0 or opposite_index == map_length:
                return reflection_index + 1
            
            reflection_possible = map[check_index] == map[opposite_index]
            difference+= 1
    return 0

maps = []
with open("input.txt", 'r') as file:
    map = []
    for line in file:
        line = line.strip()
        if not line:
            maps.append(map)
            map = []
        else:
            map.append(line)
    maps.append(map)

sum = 0
for map in maps:
    rotated_map = ["".join(tup) for tup in zip(*map)]
    if map_reflection:= find_reflection(map):
        sum += 100 * map_reflection
    else:
        sum+= find_reflection(rotated_map)

print(sum)
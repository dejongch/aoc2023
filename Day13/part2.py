def compare_strings(str1, str2, allow_one_char_difference):
    # Count the number of differing characters
    diff_count = sum(c1 != c2 for c1, c2 in zip(str1, str2))

    # Determine the result based on the diff_count and the boolean flag
    if diff_count == 0:
        return (True, False)
    elif diff_count == 1 and allow_one_char_difference:
        return (True, True)
    else:
        return (False, False)

def find_reflection(map):
    map_length = len(map)
    for reflection_index in range(map_length-1):
        difference = 0
        reflection_possible = True
        can_remove_smudge = True
        while reflection_possible:
            check_index = reflection_index - difference
            opposite_index = reflection_index + 1 + difference
            
            if check_index < 0 or opposite_index == map_length:
                if not can_remove_smudge:
                    return reflection_index + 1
                else:
                    reflection_possible = False
                    break
            
            check_result = compare_strings(map[check_index], map[opposite_index], can_remove_smudge)
            reflection_possible = check_result[0]
            if check_result[1]:
                can_remove_smudge = False
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

output = 0
for map in maps:
    rotated_map = ["".join(tup) for tup in zip(*map)]
    if map_reflection:= find_reflection(map):
        output += 100 * map_reflection
    else:
        output+= find_reflection(rotated_map)

print(output)
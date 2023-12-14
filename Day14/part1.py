map = []
with open("input.txt", 'r') as file:
    for line in file:
        map.append(line.strip())


def get_tilted_weight(map):
    rotated_map = ["".join(tup) for tup in zip(*map)]
    weight = 0
    num_rows = len(rotated_map[0])
    for row in rotated_map:
        hash_index = [-1] + [index for index, value in enumerate(row) if value == "#"]
        round_groups_size = [len(group) for group in row.replace(".", "").split("#")]
        for index, size in enumerate(round_groups_size):
            highest_rock = num_rows - (hash_index[index] + 1)
            weight += int((size / 2) * (2 * highest_rock - size + 1))
    return weight

print(get_tilted_weight(map))
seeds: list[int] = []
transformations: list[dict[tuple, int]] = []
with open("input.txt", 'r') as file:
    current_transform: dict[tuple, int] = {}
    for index, line in enumerate(file):
        line = line.strip()
        if index == 0:
            seeds = [int(seed) for seed in line.split(": ")[1].split()]
        else:
            if ":" in line:
                if current_transform:
                    transformations.append(current_transform)
                    current_transform = {}
            elif line:
                target, source, range_length = map(int, line.split())
                current_transform[(source, source+range_length-1)] = target - source

for transform in transformations:
    for seed_index in range(len(seeds)):
        seed = seeds[seed_index]
        for (minimum, maximum), difference in transform.items():
            if seed <= maximum and seed >= minimum:
                seed+=difference
                seeds[seed_index] = seed
                break

print(min(seeds))
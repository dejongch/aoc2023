def find_range_intersection(range1, range2):
    start1, end1 = range1
    start2, end2 = range2

    # Check for no overlap
    if end1 < start2 or end2 < start1:
        return None

    # Calculate the intersection
    start_intersection = max(start1, start2)
    end_intersection = min(end1, end2)

    return start_intersection, end_intersection

seeds: list[tuple[int, int]] = []
transformations: list[dict[tuple, int]] = []
with open("input.txt", 'r') as file:
    current_transform: dict[tuple, int] = {}
    for index, line in enumerate(file):
        line = line.strip()
        if index == 0:
            seeds_input = [int(seed) for seed in line.split(": ")[1].split()]
            for seed_input_index in range(0, len(seeds_input), 2):
                seed_start = seeds_input[seed_input_index]
                seed_end = seed_start + seeds_input[seed_input_index+1]
                seeds.append((seed_start, seed_end))
        else:
            if ":" in line:
                if current_transform:
                    transformations.append(current_transform)
                    current_transform = {}
            elif line:
                target, source, range_length = map(int, line.split())
                current_transform[(source, source+range_length-1)] = target - source

current_ranges: list[tuple[int, int]] = seeds

for transform in transformations:
    new_ranges = []
    for initial_seed_range in current_ranges:
        leftover_seed_ranges = [initial_seed_range]
        for transform_range, difference in transform.items():
            new_leftovers = []
            for seed_range in leftover_seed_ranges:
                if intersect_range:= find_range_intersection(seed_range, transform_range):
                    seed_range_start, seed_range_end = seed_range
                    intersect_start, intersect_end = intersect_range
                    new_ranges.append((intersect_start+difference, intersect_end+difference))
                    if seed_range_start < intersect_start:
                        new_leftovers.append((seed_range_start, intersect_start-1))
                    if seed_range_end > intersect_end:
                        new_leftovers.append((intersect_end+1, seed_range_end))
                else:
                    new_leftovers.append(seed_range)
            leftover_seed_ranges = new_leftovers
        new_ranges += leftover_seed_ranges
    current_ranges = new_ranges

print(min([range[0] for range in current_ranges]))

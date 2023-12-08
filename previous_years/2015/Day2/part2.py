from math import prod

with open("input.txt", 'r') as file:
    total = 0
    for line in file:
        dimensions = [int(dimension) for dimension in line.strip().split("x")]
        dimensions.sort()
        
        total += dimensions[0] * 2 + dimensions[1] * 2 + prod(dimensions)

    print(total)
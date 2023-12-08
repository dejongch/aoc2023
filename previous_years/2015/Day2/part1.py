with open("input.txt", 'r') as file:
    total = 0
    for line in file:
        length, width, height = [int(dimension) for dimension in line.strip().split("x")]
        front = width * height
        top = width * length
        side = height * length
        total += 2*front + 2*top + 2*side + min([front, top, side])
    print(total)
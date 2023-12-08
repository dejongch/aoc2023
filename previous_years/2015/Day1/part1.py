with open("input.txt", 'r') as file:
    for line in file:
        floor = 0
        for char in line:
            if char == "(":
                floor+=1
            else:
                floor-=1
        print(floor)
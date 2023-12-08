with open("input.txt", 'r') as file:
    for line in file:
        floor = 0
        for index, char in enumerate(line):
            if char == "(":
                floor+=1
            else:
                floor-=1
            
            if floor == -1:
                print(index+1)
                break
items = []

with open("input.txt", 'r') as file:
    for line in file:
        items += line.strip().split(",")

sum = 0
for item in items:
    current_value = 0
    for char in item:
        current_value += ord(char)
        current_value = current_value * 17
        current_value = current_value % 256
    sum += current_value

print(sum)

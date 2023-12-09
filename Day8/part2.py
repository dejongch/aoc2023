import re
import math

def lcm_of_list(numbers):
    if len(numbers) < 2:
        return number[0]

    lcm = numbers[0]
    for number in numbers[1:]:
        lcm = lcm * number // math.gcd(lcm, number)

    return lcm

regex = r"(...) = \((...), (...)\)"
nodes = {}
current_locations = []
with open("input.txt", 'r') as file:
    for index, line in enumerate(file):
        line = line.strip()
        if not index:
            commands = [int(command) for command in line.replace("L", "0").replace("R", "1")]
        elif line:
            location, left_command, right_command = re.match(regex, line).groups()
            nodes[location] = (left_command, right_command)
            if location[2] == "A":
                current_locations.append(location)

command_index = 0
steps = 0
number_of_commands = len(commands)
number_of_current_locations = len(current_locations)
first_hit_step = {}
answer_found = False
while not answer_found:
    steps+=1
    if command_index == number_of_commands:
        command_index = 0
    for current_location_index in range(number_of_current_locations):
        current_location = current_locations[current_location_index]
        current_locations[current_location_index] = nodes[current_location][commands[command_index]]

        if current_locations[current_location_index].endswith("Z"):
            if first_hit_step.get(current_location_index) is None:
                first_hit_step[current_location_index] = steps
                values = list(first_hit_step.values())
                if len(values) == number_of_current_locations:
                    print(lcm_of_list(values))
                    answer_found = True
                    break
    command_index+=1

print(steps)


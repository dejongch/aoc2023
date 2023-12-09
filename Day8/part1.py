import re

regex = r"(...) = \((...), (...)\)"
nodes = {}
with open("input.txt", 'r') as file:
    for index, line in enumerate(file):
        line = line.strip()
        if not index:
            commands = [int(command) for command in line.replace("L", "0").replace("R", "1")]
        elif line:
            location, left_command, right_command = re.match(regex, line).groups()
            nodes[location] = (left_command, right_command)

current_location = "AAA"
end_location = "ZZZ"
command_index = 0
steps = 0
number_of_commands = len(commands)

while current_location != end_location:
    if command_index == number_of_commands:
        command_index = 0
    current_location = nodes[current_location][commands[command_index]]
    command_index+=1
    steps+=1

print(steps)


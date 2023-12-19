import re
from turtle import update

workflows = {}


check_regex = r"([xmas])([<>])(\d*):([a-zA-Z]+)"
workflow_regex = r"(.*){(.*)}"

operation_min_max = {
    ">": (max, 1),
    "<": (min, -1)
}

opposite_operation = {
    ">": "<",
    "<": ">"
}

def update_range(range, operation, limit):
    low = operation_min_max[operation][0](range[0], limit+operation_min_max[operation][1])
    high = operation_min_max[operation][0](range[1], limit+operation_min_max[operation][1])
    
    return (low, high)


with open("input.txt", 'r') as file:
    checking_workflows = True
    for line in file:
        line = line.strip()
        if not line:
            break

        name, details = re.match(workflow_regex, line).groups()
        details = details.split(",")
        checks = []
        previous_operations = []
        for detail in details[:-1]:
            part_cat, operation, operation_limit, destination = re.match(check_regex, detail).groups()
            operation_limit = int(operation_limit)
            operations = [(part_cat, operation, operation_limit)] + previous_operations
            checks.append((operations, destination))
            previous_operations.append((part_cat, opposite_operation[operation], operation_limit + operation_min_max[operation][1]))
        checks.append((previous_operations, details[-1]))

        workflows[name] = checks

def get_accepted_parts(starting_part):
    parts = [(starting_part, "in")]
    accepted_parts = []
    while parts:
        part, location = parts.pop()

        for operations, destination in workflows[location]:
            if destination != "R":
                new_part = part.copy()
                for part_cat, operation, operation_limit in operations:
                    new_range = update_range(new_part[part_cat], operation, operation_limit)
                    if not new_range:
                        break
                    new_part[part_cat] = new_range
                if destination == "A":
                    accepted_parts.append(new_part)
                else:
                    parts.append((new_part, destination))
    return accepted_parts

def calculate_part_range_value(part):
    x = part["x"][1] - part["x"][0] + 1
    m = part["m"][1] - part["m"][0] + 1
    a = part["a"][1] - part["a"][0] + 1
    s = part["s"][1] - part["s"][0] + 1
    return x * m * a * s

accepted_parts = get_accepted_parts({
    "x": (1,4000),
    "m": (1,4000),
    "a": (1,4000),
    "s": (1,4000),
})

total = 0
for part in accepted_parts:
    total += calculate_part_range_value(part)

print(total)     
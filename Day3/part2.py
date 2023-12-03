from math import prod

def parse_input():
    parsed_input = []
    with open("input.txt", 'r') as file:
        for line in file:
            parsed_input.append(line.replace("\n", "."))
    return parsed_input

def find_result(input):
    gear_values = {}
    num_rows = len(input)
    num_columns = len(input[0])

    for row in range(num_rows):
        current_part_num = ""
        current_gears = {}

        for column in range(num_columns):
            current_char: str = input[row][column]

            if not current_char.isdigit():
                for gear in current_gears.keys():
                    if not gear_values.get(gear):
                        gear_values[gear] = []

                    gear_values[gear].append(int(current_part_num))

                current_part_num = ""
                current_gears = {}

            elif current_char.isdigit():
                low_check_row = max(row-1, 0)
                high_check_row = min(num_rows, row+2)

                for check_row in range(low_check_row, high_check_row):

                    low_check_column = max(column - 1 if not current_part_num else column + 1, 0)
                    high_check_column = min(num_columns, column+2)

                    for check_column in range(low_check_column, high_check_column):
                        if input[check_row][check_column] == "*":
                            current_gears[(check_row, check_column)] = True

                current_part_num += current_char
    
    sum = 0

    for gear, values in gear_values.items():
        if len(values) == 2:
            sum += prod(values)
            
    return sum

input = parse_input()
sum = find_result(input)
print(f"Part sum is {sum}")
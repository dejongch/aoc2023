def parse_input():
    parsed_input = []
    with open("input.txt", 'r') as file:
        for line in file:
            parsed_input.append(line.replace("\n", "."))
    return parsed_input

def check_for_symbol(row, column):
    char = input[row][column]
    return (
        not char.isdigit()
        and char != "."
    )

def get_part_sum(input: list[list[str]]):
    sum = 0
    num_rows = len(input)
    num_columns = len(input[0])
    for row in range(num_rows):
        current_part_num = ""
        part_valid = False
        for column in range(num_columns):
            current_char: str = input[row][column]
            if not current_char.isdigit():
                if part_valid:
                    sum += int(current_part_num)
                current_part_num = ""
                part_valid = False
            elif current_char.isdigit():
                if not part_valid:
                    low_check_row = max(row-1, 0)
                    high_check_row = min(num_rows, row+2)
                    for check_row in range(low_check_row, high_check_row):
                        if not part_valid:
                            low_check_column = max(column - 1 if not current_part_num else column + 1, 0)
                            high_check_column = min(num_columns, column+2)
                            for check_column in range(low_check_column, high_check_column):
                                if check_for_symbol(check_row, check_column):
                                    part_valid = True
                                    break
                current_part_num += current_char
    return sum

input = parse_input()
sum = get_part_sum(input)
print(f"Part sum is {sum}")

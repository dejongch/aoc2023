NUMBER_DICT = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
               'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def extract_digit(current_char, current_string):
    if current_char.isdigit():
        return current_char

    for word, digit in NUMBER_DICT.items():
        if word in current_string:
            return digit

    return ""

def get_calibration_value(line):
    start_digit = ""
    end_digit = ""
    current_string = ""

    # Loop from the start to find the first digit or spelled-out number
    for char in line:
        current_string += char
        start_digit = extract_digit(char, current_string)
        if start_digit:
            break

    current_string = ""

    # Loop from the end to find the last digit or spelled-out number
    for char in reversed(line):
        current_string = char + current_string
        end_digit = extract_digit(char, current_string)
        if end_digit:
            break

    # Check if we found at least one digit
    if start_digit and end_digit:
        # Construct a string from the first and last digits and convert it to an integer
        return int(start_digit + end_digit)

    return 0  # Return 0 if no digits are found

def get_calibration_sum(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            calibration_value = get_calibration_value(line)
            total_sum += calibration_value

    return total_sum

if __name__ == "__main__":
    input_file = "input.txt"
    result = get_calibration_sum(input_file)
    print(f"The sum of all calibration values is: {result}")

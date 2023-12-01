def get_calibration_sum(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            digits = [char for char in line if char.isdigit()]
            if digits:
                # Take the first and last digits and form a two-digit number
                calibration_value = int(digits[0] + digits[-1])
                total_sum += calibration_value

    return total_sum

if __name__ == "__main__":
    input_file = "input.txt"
    result = get_calibration_sum(input_file)
    print(f"The sum of all calibration values is: {result}")

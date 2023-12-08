import math
with open("input.txt", 'r') as file:
    time_race_numbers = []
    for line in file:
        time_race_numbers.append(
            [int(line.strip().split(":")[1].replace(" ", ""))]
        )
    
    races = []
    for index in range(len(time_race_numbers[0])):
        races.append((time_race_numbers[0][index], time_race_numbers[1][index]))

margin_of_error = 1
for (time, record_distance) in races:
    required_distance = record_distance + 1
    low_beat = math.ceil((time - math.sqrt(time**2 - 4 * required_distance))/2)
    high_beat = math.floor((time + math.sqrt(time**2 - 4 * required_distance))/2)
    number_of_winning_options = high_beat-low_beat+1
    margin_of_error = margin_of_error * (number_of_winning_options)

print(margin_of_error)
def get_game_power(line):
    game_results = line.split(": ")[1]
    games = game_results.split("; ")

    min_cubes = {
    "red": 0,
    "green": 0,
    "blue": 0
}

    for game in games:
        for pull in game.split(", "):
            count, colour = pull.split(" ")
            min_cubes[colour] = max(min_cubes[colour], int(count))
                
    return min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]


def get_game_power_sum(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            game_power = get_game_power(line.strip())
            total_sum += game_power
    return total_sum


if __name__ == "__main__":
    input_file = "input.txt"
    result = get_game_power_sum(input_file)
    print(f"The sum of all game powers is: {result}")
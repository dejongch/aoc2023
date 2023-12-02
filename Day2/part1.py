MAX_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def get_valid_game_id(line):
    game_designation, game_results = line.split(": ")
    game_id = int(game_designation.split(" ")[1])
    games = game_results.split("; ")

    for game in games:
        for pull in game.split(", "):
            count, colour = pull.split(" ")
            if int(count) > MAX_CUBES[colour]:
                return 0
    return game_id


def get_game_id_sum(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            game_id = get_valid_game_id(line.strip())
            total_sum += game_id
    return total_sum


if __name__ == "__main__":
    input_file = "input.txt"
    result = get_game_id_sum(input_file)
    print(f"The sum of all valid game ids is: {result}")
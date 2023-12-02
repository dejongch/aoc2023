def is_possible_game(game, counts):
    for pull in game:
        cubes = pull.split(',')
        for cube_info in cubes:
            count, color = cube_info.strip().split()
            count = int(count)
            if counts[color] < count:
                return False
    return True

def main():
    target_counts = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = []
    
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split(':')
        game_id = int(parts[0].split()[1])
        game_info = parts[1].strip().split(';')
        if is_possible_game(game_info, target_counts):
            possible_games.append(game_id)

    print("The sum of the IDs of possible games is:", sum(possible_games))

if __name__ == "__main__":
    main()

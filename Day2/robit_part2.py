def min_cubes_for_game(game):
    min_set = {'red': 0, 'green': 0, 'blue': 0}

    for pull in game:
        cubes = [cube.split() for cube in pull.split(',') if cube.strip()]
        for count, color in cubes:
            count = int(count)
            min_set[color] = max(min_set[color], count)

    return min_set

def power_of_set(cubes):
    return cubes['red'] * cubes['green'] * cubes['blue']

def main():
    total_power = 0

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split(':')
        if len(parts) != 2:
            continue  # Skip lines without the expected format
        _, game_info = parts
        min_cubes = min_cubes_for_game(game_info.split(';'))
        total_power += power_of_set(min_cubes)

    print("The sum of the power of the minimum sets is:", total_power)

if __name__ == "__main__":
    main()

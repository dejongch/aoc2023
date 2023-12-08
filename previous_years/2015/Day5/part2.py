nice_count = 0
with open("input.txt", 'r') as file:
    for line in file:
        has_repeat = False
        has_spaced_double = False

        letter_combo_index = {}
        line = line.strip()
        for index, char in enumerate(line):
            if not has_repeat and index < len(line) - 1:
                combo = char + line[index+1]
                if (combo_index:= letter_combo_index.get(combo)) is None:
                    letter_combo_index[combo] = index
                elif index - combo_index > 1:
                    has_repeat = True
            if not has_spaced_double and index < len(line) - 2:
                has_spaced_double = char == line[index + 2]
        if has_repeat and has_spaced_double:
            nice_count += 1

print(nice_count)


banned_combo = {
    "a": "b",
    "c": "d",
    "p": "q",
    "x": "y"
}
nice_count = 0
with open("input.txt", 'r') as file:
    for line in file:
        vowel_count = 0
        has_double_letter = False
        found_banned_combo = False

        for index, char in enumerate(line.strip()):
            is_last_letter = index == len(line) - 1
            if vowel_count < 3 and char in "aeiou":
                vowel_count += 1
            if not is_last_letter:
                if not has_double_letter and char == line[index + 1]:
                    has_double_letter = True
                banned_next_letter = banned_combo.get(char)
                if  banned_next_letter and line[index+1] == banned_next_letter:
                    found_banned_combo = True
                    break
        if not found_banned_combo and has_double_letter and vowel_count == 3:
            nice_count += 1

print(nice_count)


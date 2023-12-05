def parse_input():
    parsed_input = []
    with open("input.txt", 'r') as file:
        for line in file:
            card_values = line.strip().split(": ")[1]
            winning_values, scratched_values = card_values.split(" | ")
            card_input = {
                "winning_numbers": set([int(value) for value in winning_values.split() if value]),
                "numbers": set([int(value) for value in scratched_values.split() if value])
            }
            parsed_input.append(card_input)
    return parsed_input


def get_total_score(input: list[dict[str, set]]):
    sum = 0
    for card_input in input:
        num_winners = len(card_input["winning_numbers"].intersection(card_input["numbers"]))
        if num_winners > 0:
            sum+= 2**(num_winners - 1)
    return sum


print(get_total_score(parse_input()))
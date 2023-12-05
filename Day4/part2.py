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
    num_cards = len(input)
    num_each_scratch_card = [1]*num_cards
    for index, card_input in enumerate(input):
        num_winners = len(card_input["winning_numbers"] & card_input["numbers"])
        for x in range(index+1, index+num_winners+1):
            if x < num_cards:
                num_each_scratch_card[x] += num_each_scratch_card[index]
    return sum(num_each_scratch_card)


print(get_total_score(parse_input()))

passed = [97,0,2,0,1,1884,134,17,1997,36,0,2,2022,10,1,0,2002,20,12,0,0,0,1,2003,24,7,1,2004,30,0,1,1995,39,0,0,0,1,2012,12,9,2,2028,7,2015,19,0,1,1977,56,2]
failed = [3,3,1,1,0,145,18,0,39,2,2,0,14,3,2,2,33,13,1,1,1,1,0,35,3,1,0,31,1,1,0,40,1,1,1,1,0,23,9,2,0,7,0,20,1,1,0,60,2,0]

third_try_failures = []

for x in range(50):
    if passed[x] > 1000:
        first_run = x
        while failed[x] != 0 and x - first_run < 3:
            x+=1
        third_try_failures.append(failed[x])

percentage_with_rerun = sum(third_try_failures) / (2212 * 11) * 100

print(third_try_failures)
print(100-percentage_with_rerun)

percentage = sum(failed) / sum(passed+failed) * 100
print(len(passed))
print (sum(passed))
print (sum(failed))
print(100-percentage)
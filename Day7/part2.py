from collections import Counter

alphabet = "J23456789TQKA"

def convert_to_base_10(hand):
    # Reverse the poker hand string to simplify indexing
    reversed_str = hand[::-1]
    
    base_10_number = 0
    base = 13

    for index, char in enumerate(reversed_str):
        # Find the index of the character in the alphabet
        char_index = alphabet.index(char)
        # Convert to base 10 using the formula: base^index * char_index
        base_10_number += (base ** index) * char_index

    return base_10_number


highest = convert_to_base_10("AAAAA")

def get_hand_value(hand):
    value = convert_to_base_10(hand)
    counter = Counter(hand)
    counts = counter.most_common()
    jokers = counter.get("J", 0)

    highest_dup = counts[0][1]
    second_dup = counts[1][1] if len(counts) > 1 else 0
    

    if("J" in [counts[0][0], counts[1][0] if len(counts)> 1 else None]):
        highest_dup += second_dup
        second_dup = counts[2][1] if len(counts) > 2 else 0
    else:
        highest_dup += jokers

    if highest_dup >= 4:
        return value + highest * (highest_dup + 1)
    if highest_dup == 3:
        return value + highest * (second_dup + 2)
    if highest_dup == 2:
        return value + highest * (second_dup)
    return value

hands = []
with open("input.txt", 'r') as file:
    for line in file:
        hand,bet = line.strip().split()
        hands.append((get_hand_value(hand), int(bet)))

sorted_hands = sorted(hands, key=lambda x: x[0])

total = 0

for index, (hand, bet) in enumerate(sorted_hands):
    total += ((index + 1) * bet)

print(total)


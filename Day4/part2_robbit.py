def simulate_winning(cards):
    total_cards = len(cards)
    copies = [1] * total_cards  # Initialize with one copy for each original card

    for i in range(total_cards):
        winning_numbers, your_numbers = cards[i]
        matches = len(set(winning_numbers) & set(your_numbers))

        for j in range(i + 1, min(i + 1 + matches, total_cards)):
            copies[j] += copies[i]

    return sum(copies)

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    cards = []
    for line in lines:
        card_data = line.strip().split(": ")[1]
        winning_numbers = list(map(int, filter(None, card_data.split(" | ")[0].split())))
        your_numbers = list(map(int, filter(None, card_data.split(" | ")[1].split())))
        cards.append((winning_numbers, your_numbers))

    total_scratchcards = simulate_winning(cards)
    print(f"The total scratchcards are: {total_scratchcards}")

if __name__ == "__main__":
    main()

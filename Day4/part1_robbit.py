def calculate_points(card):
    winning_numbers, your_numbers = card
    points = 0

    for number in your_numbers:
        if number in winning_numbers:
            points += 1

    return 2 ** (points - 1) if points > 0 else 0

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    cards = []
    for line in lines:
        # Split the line into card number and numbers on the card
        card_number, card_data = line.strip().split(": ")
        card_number = int(card_number.split()[-1])  # Extract the card number
        winning_numbers = list(map(int, filter(None, card_data.split(" | ")[0].split())))
        your_numbers = list(map(int, filter(None, card_data.split(" | ")[1].split())))
        cards.append((winning_numbers, your_numbers))

    total_points = sum(calculate_points(card) for card in cards)
    print(f"The total points for the scratchcards are: {total_points}")

if __name__ == "__main__":
    main()

import random

def fisher_yates_shuffle(arr):
  
    n = len(arr)

    for i in range(n - 1, 0, -1):
        r = random.randint(0, i)
        arr[i], arr[r] = arr[r], arr[i]


def main():
    # All suits in a standard deck
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    # All ranks in a standard deck
    ranks = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]

    deck = []

    # Create the full deck (52 cards)
    for suit in suits:
        for rank in ranks:
            deck.append(rank + " of " + suit)

    print("Deck before shuffle:")
    print(deck)

    # Shuffle the deck
    fisher_yates_shuffle(deck)

    print("\nDeck after shuffle:")
    print(deck)


if __name__ == "__main__":
    main()
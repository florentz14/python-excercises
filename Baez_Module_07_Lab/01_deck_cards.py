# -------------------------------------------------
# File Name: 01_deck_cards.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 07 Lab
# Description: Deck Cards Program. Uses a dictionary to simulate a standard
#              deck of poker cards with numeric values similar to Blackjack:
#              • Numeric cards: value as printed (e.g., 2 of spades = 2).
#              • Jacks, queens, kings: value 10.
#              • Aces: value 1 (or 11 by choice; program uses 1).
#              Key-value pairs use card name as key and numeric value as value
#              (e.g., 'Queen of Hearts': 10). Prompts for number of cards to
#              deal, randomly deals that many cards, and displays card names
#              and total numeric value. Functions: main, create_deck, deal_cards.
# -------------------------------------------------

import random

# =============================================================================
# EXERCISE 1: Deck Cards Program
# =============================================================================

def create_deck() -> dict[str, int]:
    """
    Create a dictionary representing a standard deck of poker cards.

    Returns:
        dict: Dictionary with card names as keys and numeric values as values
    """
    # Define suits and ranks
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King']

    # Initialize empty deck
    deck = {}

    # Loop (for): Iterate through each suit
    for suit in suits:
        # Loop (for): Iterate through each rank
        for rank in ranks:
            # Create card name
            card_name = f"{rank} of {suit}"

            # Assign numeric value based on rank
            if rank == 'Ace':
                value = 1  # Aces are valued at 1
            elif rank in ['Jack', 'Queen', 'King']:
                value = 10  # Face cards are valued at 10
            else:
                value = int(rank)  # Numeric cards have their printed value

            # Add card to deck dictionary
            deck[card_name] = value

    return deck


def deal_cards(deck: dict[str, int], num_cards: int) -> tuple[list[str], int]:
    """
    Deal a specified number of cards randomly from the deck.

    Args:
        deck (dict): Dictionary representing the deck of cards
        num_cards (int): Number of cards to deal

    Returns:
        tuple: (list of card names, total numeric value of the hand)
    """
    # Convert deck dictionary keys to a list for random selection
    card_list = list(deck.keys())

    # Randomly select cards (without replacement)
    hand = random.sample(card_list, min(num_cards, len(card_list)))

    # Calculate total value of the hand
    total_value = sum(deck[card] for card in hand)

    return hand, total_value


def main() -> None:
    """
    Main function to run the deck cards program.
    """
    print("=" * 60)
    print("EXERCISE 1: Deck Cards Program")
    print("=" * 60)

    # Create the deck
    deck = create_deck()
    print(f"Deck created with {len(deck)} cards.")

    # Get number of cards to deal
    # Try-except block: Handles exceptions that may occur during input conversion
    try:
        num_cards = int(input("\nEnter the number of cards to deal: "))

        # Validate input
        if num_cards < 1:
            print("Error: Number of cards must be at least 1.")
        elif num_cards > len(deck):
            print(f"Error: Cannot deal more than {len(deck)} cards.")
        else:
            # Deal cards
            hand, total_value = deal_cards(deck, num_cards)

            # Display results
            print("\n" + "=" * 60)
            print("DEALT HAND")
            print("=" * 60)
            print("Cards dealt:")
            for i, card in enumerate(hand, 1):
                print(f"  {i}. {card} (value: {deck[card]})")

            print(f"\nTotal numeric value of the hand: {total_value}")

    except ValueError:
        # Handle invalid numeric input (e.g., non-numeric characters)
        print("Error: Please enter a valid integer.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error: {e}")


# Run Exercise 1
main()

print()

# =============================================================================
# CITATIONS
# =============================================================================
print("Citations:")
print("1. Dictionary Operations in Python:")
print("   - Dictionary creation, access, keys()")
print("   Source: Python Documentation - Dictionaries")
print("   https://docs.python.org/3/tutorial/datastructures.html#dictionaries")
print()
print("2. Random Module:")
print("   - random.sample() for random selection without replacement")
print("   Source: Python Documentation - Random Module")
print("   https://docs.python.org/3/library/random.html")
print()
print("3. Card Game Values:")
print("   - Blackjack card values: numeric cards (2-10), face cards (10), aces (1 or 11)")
print("   Source: Standard Blackjack card values")

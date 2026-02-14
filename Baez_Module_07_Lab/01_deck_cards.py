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

# Import the random module to generate random numbers
import random


# Function: Create a dictionary representing a standard deck of poker cards
# dict[str, int]: Dictionary with card names as keys and numeric values as values
def create_deck() -> dict[str, int]:
    # Define suits and ranks
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] # List of suits
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] # List of ranks

    # Initialize empty deck
    deck: dict[str, int] = {} # Initialize an empty dictionary to store the deck of cards

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

    return deck # Return the deck of cards


# Function: Deal a specified number of cards randomly from the deck
# dict[str, int]: Dictionary with card names as keys and numeric values as values
# int: Number of cards to deal from the deck
# tuple[list[str], int]: Tuple with a list of card names dealt and the total numeric value of the hand
def deal_cards(deck: dict[str, int], num_cards: int) -> tuple[list[str], int]:
    card_list: list[str] = list(deck.keys()) # Convert the deck dictionary keys to a list for random selection

    hand: list[str] = random.sample(card_list, min(num_cards, len(card_list))) # Randomly select cards (without replacement)

    total_value: int = sum(deck[card] for card in hand) # Calculate the total value of the hand

    return hand, total_value # Return the list of card names dealt and the total numeric value of the hand


# Function: Main function to run the deck cards program
# None: No return value
def main() -> None:
    print("=" * 60)
    print("EXERCISE 1: Deck Cards Program")
    print("=" * 60)

    deck: dict[str, int] = create_deck() # Create the deck
    print(f"Deck created with {len(deck)} cards.") # Display the number of cards in the deck

    # Try-except block: Handles exceptions that may occur during input conversion
    try:
        num_cards = int(input("\nEnter the number of cards to deal: ")) # Get the number of cards to deal

        # Input validation: Do not accept a number less than 1
        if num_cards < 1: # Check if the number of cards is less than 1
            print("Error: Number of cards must be at least 1.") # Display an error message
        elif num_cards > len(deck): # Check if the number of cards is greater than the number of cards in the deck  
            print(f"Error: Cannot deal more than {len(deck)} cards.") # Display an error message
        else: # If the number of cards is valid, deal the cards
            # Call the deal_cards function to deal the cards
            hand, total_value = deal_cards(deck, num_cards) # Deal the cards

            # Display results
            print("\n" + "=" * 60)
            print("DEALT HAND") # Display the title
            print("=" * 60)
            print("Cards dealt:") # Display the cards dealt
            
            # Loop (for): Iterate through each card in the hand
            for i, card in enumerate(hand, 1): # Display the card and its value
                print(f"  {i}. {card} (value: {deck[card]})") # Display the card and its value

            print(f"\nTotal numeric value of the hand: {total_value}") # Display the total numeric value of the hand

    except ValueError:
        # Handle invalid numeric input (e.g., non-numeric characters)
        print("Error: Please enter a valid integer.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error: {e}")


# Run the main function to run the deck cards program
# None: No return value
main()

print() # Print a blank line
print("=" * 60)
print("END OF PROGRAM")
print("=" * 60)

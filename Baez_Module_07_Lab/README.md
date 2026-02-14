# Baez_Module_07_Lab

Module 7 Lab: Lists and data structures.

## Note on try-except Blocks

A `try-except` block has been added to all programs in this module. **Reasons:**

1. **Input validation**: `float()` and `int()` raise `ValueError` when the user enters non-numeric input (e.g., letters or empty input). The try-except catches this and displays a friendly error message instead of crashing.
2. **Robustness**: Prevents the program from terminating unexpectedly due to invalid or unexpected input.
3. **User experience**: Prompts the user to re-enter valid data rather than exiting with a traceback.

## Files

| File | Content |
|------|---------|
| `01_deck_cards.py` | Deck of cards |
| `02_names_and_birthdays.py` | Names and birthdays |
| `03_names_and_birthdays_v2.py` | Names and birthdays v2 (tabular view of dictionary) |

## Citations

### `01_deck_cards.py`
- **Dictionary Operations in Python**: Dictionary creation, access, keys(). Source: [Python Documentation - Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- **Random Module**: random.sample() for random selection without replacement. Source: [Python Documentation - Random Module](https://docs.python.org/3/library/random.html)
- **Card Game Values**: Blackjack card values: numeric cards (2-10), face cards (10), aces (1 or 11). Source: Standard Blackjack card values

### `02_names_and_birthdays.py` / `03_names_and_birthdays_v2.py`
- **Dictionary Operations in Python**: Dictionary creation, access, update, and deletion; Dictionary methods: keys(), values(), items(). Source: [Python Documentation - Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- **Menu-Driven Programs**: Design pattern for interactive programs with multiple options. Source: Common programming design pattern

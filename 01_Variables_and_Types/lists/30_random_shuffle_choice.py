# -------------------------------------------------
# File Name: 30_random_shuffle_choice.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Demonstrates random.shuffle(), random.choice(),
# -------------------------------------------------

import random

original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original:", original)

# Shuffle in place
shuffled = original.copy()
random.shuffle(shuffled)
print("Shuffled:", shuffled)

# Random choice
print("Random choice:", random.choice(original))
print("Random sample of 3:", random.sample(original, 3))
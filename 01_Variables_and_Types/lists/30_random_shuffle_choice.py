# shuffle, choice

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
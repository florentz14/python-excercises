# -------------------------------------------------
# File Name: 38_advanced_set_comprehension.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Advanced set comprehension examples: squares, evens,
# -------------------------------------------------

print("Advanced Set Comprehension")
print("-" * 40)

# Squares of numbers
nums = [1, 2, 3, 4, 5]
squares = {x**2 for x in nums}
print("Squares of", nums, ":", squares)
print()

# Even numbers only
evens = {x for x in range(10) if x % 2 == 0}
print("Evens 0-9:", evens)
print()

# Vowel filtering from string
text = "Hello World"
vowels = {'a', 'e', 'i', 'o', 'u'}
vowels_in_text = {c.lower() for c in text if c.lower() in vowels}
print("Text:", text)
print("Vowels in text:", vowels_in_text)
print()

# Lowercase normalization (unique lowercase words)
words = ["Apple", "banana", "APPLE", "Banana", "cherry"]
normalized = {w.lower() for w in words}
print("Words:", words)
print("Normalized (unique lowercase):", normalized)
print()

# Length-based: words with more than 4 chars
long_words = {w for w in words if len(w) > 4}
print("Words with len > 4:", long_words)

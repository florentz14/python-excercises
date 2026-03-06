# -------------------------------------------------
# File Name: 65_for_count_vowels_with_input.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Date: Module 04 Lab (added)
# Description: Prompt the user for a word and count vowels using a for loop.
# -------------------------------------------------

print("=" * 40)
print("For #4 – Count Vowels (with input)")
print("=" * 40)

# Prompt the user for a word and convert to lowercase
text = input("Enter a word: ").lower()

# Vowels to check
vowels = "aeiou"
count = 0

# Loop: count occurrences of vowels in the text
for ch in text:
    if ch in vowels:
        count += 1

# Print result
print("Vowel count:", count)
print("=" * 40)

# -------------------------------------------------
# File Name: 75_for_count_vowels.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Count vowels with input.
# -------------------------------------------------

print("=" * 40)
print("For #4 – Count Vowels (with input)")
print("=" * 40)

text = input("Enter a word: ").lower()

vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count)
print("=" * 40)

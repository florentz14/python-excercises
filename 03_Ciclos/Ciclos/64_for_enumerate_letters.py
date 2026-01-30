# -------------------------------------------------
# File Name: 64_for_enumerate_letters.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Date: Module 04 Lab (added)
# Description: Use enumerate to iterate over letters of a word and print index and character.
# -------------------------------------------------

print("=" * 40)
print("For #3 – Enumerate Letters")
print("=" * 40)

word = "CODE"

# Loop: enumerate returns (index, character)
for index, ch in enumerate(word):
    print(index, ch)

print("=" * 40)

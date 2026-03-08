# -------------------------------------------------
# File Name: 40_for_count_letters.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Count letters in word.
# -------------------------------------------------

word = "Programming"
count = 0

for letter in word:
    count = count + 1

print(f"The word '{word}' has {count} letters")

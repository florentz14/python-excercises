"""For loop: Count letters in word.
Counts characters by iterating over string.
"""
# Author: Florentino Báez


word = "Programming"
count = 0

for letter in word:
    count = count + 1

print(f"The word '{word}' has {count} letters")

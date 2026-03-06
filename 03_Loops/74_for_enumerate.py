"""For loop: enumerate letters.
Uses enumerate() to print index and character of a word.
"""
# Author: Florentino Báez


print("=" * 40)
print("For #3 – Enumerate Letters")
print("=" * 40)

word = "CODE"

# enumerate returns (index, character)
for index, ch in enumerate(word):
    print(index, ch)

print("=" * 40)

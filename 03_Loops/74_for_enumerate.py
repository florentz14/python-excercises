# -------------------------------------------------
# File Name: 74_for_enumerate.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: enumerate letters.
# -------------------------------------------------

print("=" * 40)
print("For #3 – Enumerate Letters")
print("=" * 40)

word = "CODE"

# enumerate returns (index, character)
for index, ch in enumerate(word):
    print(index, ch)

print("=" * 40)

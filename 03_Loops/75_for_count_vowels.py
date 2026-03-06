"""For loop: Count vowels with input.
User enters word; counts vowels (a,e,i,o,u).
"""
# Author: Florentino Báez


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

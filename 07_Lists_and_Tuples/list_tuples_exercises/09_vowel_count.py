# -------------------------------------------------
# File Name: 09_vowel_count.py
# Description: Count each vowel in word
# -------------------------------------------------

word = input("Enter a word: ").lower()
vowels = "aeiou"
for v in vowels:
    print(f"{v}: {word.count(v)}")

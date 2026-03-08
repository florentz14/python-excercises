# -------------------------------------------------
# File Name: 08_palindrome.py
# Description: Check if word is palindrome
# -------------------------------------------------

word = input("Enter a word: ").lower()
print("Palindrome" if word == word[::-1] else "Not palindrome")

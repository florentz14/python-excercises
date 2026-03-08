# -------------------------------------------------
# File Name: 106_word_letters_reverse.py
# Description: Print letters of word one by one, from last to first
# -------------------------------------------------

word = input("Enter a word: ")
for c in reversed(word):
    print(c)

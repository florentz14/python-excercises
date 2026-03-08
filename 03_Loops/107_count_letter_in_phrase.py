# -------------------------------------------------
# File Name: 107_count_letter_in_phrase.py
# Description: Count occurrences of letter in phrase
# -------------------------------------------------

phrase = input("Enter a phrase: ")
letter = input("Enter a letter: ")
count = phrase.lower().count(letter.lower())
print(f"The letter appears {count} time(s).")

# -------------------------------------------------
# File Name: 09_capitalize_words.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Capitalize first letter of each word (title case).
# -------------------------------------------------

def capitalize_words(s: str) -> str:
    return s.title()

def capitalize_words_manual(s: str) -> str:
    return " ".join(word.capitalize() for word in s.split())

if __name__ == "__main__":
    s = "hello world from python"
    print("Original:", s)
    print("Capitalized:", capitalize_words(s))

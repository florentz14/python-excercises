# ------------------------------------------------------------
# File: 09_capitalize_words.py
# Purpose: Capitalize each word.
# Description: First letter of each word uppercase.
# ------------------------------------------------------------

def capitalize_words(s: str) -> str:
    return s.title()

def capitalize_words_manual(s: str) -> str:
    return " ".join(word.capitalize() for word in s.split())

if __name__ == "__main__":
    s = "hello world from python"
    print("Original:", s)
    print("Capitalized:", capitalize_words(s))

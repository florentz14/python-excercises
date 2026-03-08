# -------------------------------------------------
# File Name: 32_comp_strings.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: String manipulation in comprehension (key/value expressions).
# -------------------------------------------------

print("4. String Manipulation:")
print("-" * 60)
words = ["hello", "world", "python", "dictionary"]
# Use len() in value expression
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# Transform keys using string methods (e.g., .upper())
uppercase_dict = {word.upper(): len(word) for word in words}
print(f"Uppercase keys: {uppercase_dict}")

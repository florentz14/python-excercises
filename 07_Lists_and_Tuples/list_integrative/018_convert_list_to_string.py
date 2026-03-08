# -------------------------------------------------
# File Name: 018_convert_list_to_string.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Convert List of Characters to String
# -------------------------------------------------

def chars_to_string(chars: list[str]) -> str:
    return ''.join(chars)


print(chars_to_string(['a', 'b', 'c']))  # abc

# -------------------------------------------------
# File Name: 27_substring_in_list_strings.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Check If Substring Appears in Any String in List
# -------------------------------------------------

def substring_in_list(lst: list[str], sub: str) -> bool:
    return any(sub in s for s in lst)


sample = ['red', 'black', 'white', 'green', 'orange']
print(substring_in_list(sample, 'ack'))  # True
print(substring_in_list(sample, 'abc'))  # False

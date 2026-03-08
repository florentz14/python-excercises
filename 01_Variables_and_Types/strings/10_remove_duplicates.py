# -------------------------------------------------
# File Name: 10_remove_duplicates.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Remove duplicate characters while preserving order.
# -------------------------------------------------

def remove_duplicates(s: str) -> str:
    seen = set()
    result = []
    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return "".join(result)

def remove_duplicates_dict(s: str) -> str:
    return "".join(dict.fromkeys(s))

if __name__ == "__main__":
    s = "banana"
    print("Original:", s)
    print("No duplicates:", remove_duplicates(s))
    print("dict.fromkeys:", remove_duplicates_dict(s))

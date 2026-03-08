# -------------------------------------------------
# File Name: 27_rotate_string.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Check if s2 is rotation of s1. Uses s1 in (s2+s2).
# -------------------------------------------------

def is_rotation(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s1 in (s2 + s2)

def main():
    print(is_rotation("waterbottle", "erbottlewat"))
    print(is_rotation("abc", "cab"))
    print(is_rotation("abc", "bca"))

if __name__ == "__main__":
    main()

# -------------------------------------------------
# File Name: 06_reverse_string.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Reverse a string via slicing, loop, and two pointers.
# -------------------------------------------------

def reverse_slice(s: str) -> str:
    return s[::-1]

def reverse_loop(s: str) -> str:
    return "".join(s[i] for i in range(len(s) - 1, -1, -1))

def reverse_two_pointers(s: str) -> str:
    arr = list(s)
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return "".join(arr)

if __name__ == "__main__":
    s = "hello"
    print("Original:", s)
    print("Slicing:", reverse_slice(s))
    print("Loop:", reverse_loop(s))
    print("Two pointers:", reverse_two_pointers(s))

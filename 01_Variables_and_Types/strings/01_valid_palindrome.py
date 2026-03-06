"""
Valid Palindrome Checker
========================
Topic: Strings (01_Variables_and_Types/strings)
Description: Check whether a string is a palindrome. Ignores spaces, punctuation,
and symbols. Ignores uppercase/lowercase differences.

Input:  A string (e.g. "A man, a plan, a canal: Panama")
Output: "true" or "false" (lowercase)

Complexity:
    - Time:   O(n) - Single pass with two pointers
    - Space:  O(1) - No extra storage
"""


def is_palindrome(s: str) -> bool:
    """
    Returns True if the string is a valid palindrome (alphanumeric only, case-insensitive).
    Uses two pointers: one from the left, one from the right.
    """
    l, r = 0, len(s) - 1

    while l < r:
        # Move left pointer until it points to an alphanumeric character
        while l < r and not s[l].isalnum():
            l += 1

        # Move right pointer until it points to an alphanumeric character
        while l < r and not s[r].isalnum():
            r -= 1

        # Compare characters ignoring case
        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True


if __name__ == "__main__":
    s = input()
    res = is_palindrome(s)
    print("true" if res else "false")

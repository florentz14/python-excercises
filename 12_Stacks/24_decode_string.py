# -------------------------------------------------
# File Name: 24_decode_string.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Decode nested encoded strings with stack.
# -------------------------------------------------

"""
============================================================
  DECODE STRING - Python 3.14
  Decode expressions like:
    3[a2[c]] -> accaccacc

  Encoding format:
    k[encoded_string]
  where k is a positive integer and encoded_string can be nested.

  Technique:
    - Use stacks to store previous strings and repeat counts.
    - Build current segment until ']' is reached.
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def decode_string(s: str) -> str:
    """Decode nested k[...] patterns."""
    count_stack: list[int] = []
    string_stack: list[str] = []
    current = ""
    number = 0

    for ch in s:
        if ch.isdigit():
            number = number * 10 + int(ch)
        elif ch == "[":
            count_stack.append(number)
            string_stack.append(current)
            number = 0
            current = ""
        elif ch == "]":
            repeat = count_stack.pop()
            prev = string_stack.pop()
            current = prev + current * repeat
        else:
            current += ch
    return current


def demo() -> None:
    title("DECODE STRING - Nested stack parsing")

    tests = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("10[a]", "aaaaaaaaaa"),
        ("3[z]2[2[y]pq4[2[jk]e1[f]]]ef", None),
    ]

    for encoded, expected in tests:
        result = decode_string(encoded)
        print(f"\n  Encoded: {encoded}")
        print(f"  Decoded: {result}")
        if expected is not None:
            print(f"  Expected: {expected}")
            print(f"  Match   : {result == expected}")
        else:
            print("  Expected: (long output omitted)")


if __name__ == "__main__":
    demo()

# ------------------------------------------------------------
# File: 19_naive_pattern_search.py
# Purpose: Brute force substring search.
# Description: Try each starting position. O(n*m).
# ------------------------------------------------------------

def naive_search(text: str, pattern: str) -> list[int]:
    n, m = len(text), len(pattern)
    indices = []
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            indices.append(i)
    return indices

def main():
    text, pattern = "ABABDABACDABABCABAB", "ABABCABAB"
    print(naive_search(text, pattern))

if __name__ == "__main__":
    main()

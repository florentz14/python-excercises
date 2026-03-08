# -------------------------------------------------
# File Name: 20_kmp_algorithm.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: KMP pattern search with failure (LPS) function.
# -------------------------------------------------

def build_lps(pattern: str) -> list[int]:
    """Build longest proper prefix which is also suffix array."""
    m = len(pattern)
    lps = [0] * m
    length, i = 0, 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps

def kmp_search(text: str, pattern: str) -> list[int]:
    """Return list of indices where pattern occurs in text."""
    if not pattern:
        return []
    n, m = len(text), len(pattern)
    lps = build_lps(pattern)
    indices = []
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j:
                j = lps[j - 1]
            else:
                i += 1
    return indices

def main():
    text, pattern = "ABABDABACDABABCABAB", "ABABCABAB"
    print("Indices:", kmp_search(text, pattern))

if __name__ == "__main__":
    main()

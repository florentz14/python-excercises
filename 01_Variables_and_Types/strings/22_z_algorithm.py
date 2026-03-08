# -------------------------------------------------
# File Name: 22_z_algorithm.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Z-algorithm: Z-array construction for pattern matching.
# -------------------------------------------------

def build_z_array(s: str) -> list[int]:
    """Build Z-array: Z[i] = length of longest substring starting at i that matches prefix."""
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def z_search(text: str, pattern: str) -> list[int]:
    """Find all occurrences of pattern in text using Z-algorithm."""
    concat = pattern + "$" + text
    z = build_z_array(concat)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(concat)) if z[i] == m]

def main():
    text, pattern = "GEEKS FOR GEEKS", "GEEK"
    print("Indices:", z_search(text, pattern))

if __name__ == "__main__":
    main()

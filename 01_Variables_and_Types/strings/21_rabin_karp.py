# ------------------------------------------------------------
# File: 21_rabin_karp.py
# Purpose: Rolling hash substring search.
# Description: Compute hash for pattern and each window. O(n) avg.
# ------------------------------------------------------------

def rabin_karp(text: str, pattern: str, base: int = 256, mod: int = 10**9 + 7) -> list[int]:
    """Return indices where pattern occurs using rolling hash."""
    n, m = len(text), len(pattern)
    if m > n:
        return []
    h = pow(base, m - 1, mod)
    pat_hash = win_hash = 0
    for i in range(m):
        pat_hash = (pat_hash * base + ord(pattern[i])) % mod
        win_hash = (win_hash * base + ord(text[i])) % mod
    indices = []
    for i in range(n - m + 1):
        if pat_hash == win_hash and text[i:i + m] == pattern:
            indices.append(i)
        if i < n - m:
            win_hash = (win_hash - ord(text[i]) * h) * base + ord(text[i + m])
            win_hash %= mod
    return indices

def main():
    text, pattern = "GEEKS FOR GEEKS", "GEEK"
    print("Indices:", rabin_karp(text, pattern))

if __name__ == "__main__":
    main()

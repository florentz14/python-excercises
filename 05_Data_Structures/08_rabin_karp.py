# -------------------------------------------------
# File Name: 08_rabin_karp.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Rabin-Karp algorithm for pattern matching. Uses rolling hash for efficient substring comparison. O(n + m) average, O(n*m) worst case.
# -------------------------------------------------

print("=== Advanced String Algorithms ===\n")
print("=== 1. Rabin-Karp Algorithm ===\n")


def rabin_karp(text, pattern, base=256, prime=101):
    """
    Pattern search using Rabin-Karp (rolling hash).
    Complexity: O(n + m) average, O(n * m) worst case
    """
    n = len(text)
    m = len(pattern)

    if m == 0:
        return [0]
    if m > n:
        return []

    hash_pattern = 0     # Hash of the pattern to search for
    hash_window = 0      # Hash of the current window in the text
    h = 1                # Positional value of the most significant digit
    # Compute h = base^(m-1) % prime (to remove the first character)
    for i in range(m - 1):
        h = (h * base) % prime

    # Compute initial hash of the pattern and of the first window
    for i in range(m):
        hash_pattern = (base * hash_pattern + ord(pattern[i])) % prime
        hash_window = (base * hash_window + ord(text[i])) % prime

    occurrences = []

    for i in range(n - m + 1):
        if hash_pattern == hash_window:
            # Hashes match → verify character by character
            if text[i:i+m] == pattern:
                occurrences.append(i)

        if i < n - m:
            # Rolling hash: remove first character and add the next one
            hash_window = (base * (hash_window - ord(text[i]) * h) + ord(text[i + m])) % prime
            if hash_window < 0:
                hash_window = hash_window + prime  # Correct negative hash

    return occurrences


if __name__ == "__main__":
    sample_text = "GEEKS FOR GEEKS"
    sample_pattern = "GEEK"

    print(f"Text: '{sample_text}'")
    print(f"Pattern: '{sample_pattern}'")
    rk_occurrences = rabin_karp(sample_text, sample_pattern)
    print(f"Occurrences (Rabin-Karp): {rk_occurrences}")

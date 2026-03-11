# -------------------------------------------------
# File Name: 09_z_algorithm.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Z-Algorithm for pattern search. Z[i] = longest prefix matching substring at i. Concatenate pattern+$+text; matches where Z[i]=len(pattern). O(n+m).
# -------------------------------------------------

def build_z_array(s):
    """
    Builds Z-array: Z[i] = longest common prefix length of s and s[i:].
    """
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0  # Rightmost Z-box [l, r]

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z


def z_search(text, pattern):
    """Returns list of starting indices where pattern occurs in text."""
    m = len(pattern)
    if m == 0:
        return [0]

    combined = pattern + "$" + text
    z = build_z_array(combined)

    matches = []
    for i in range(m + 1, len(combined)):
        if z[i] == m:
            matches.append(i - m - 1)

    return matches


if __name__ == "__main__":
    print("=== String Algorithms: Z-Algorithm ===\n")

    text = "ABABDABACDABABCABCABAB"
    pattern = "ABABCABAB"

    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")
    matches = z_search(text, pattern)
    print(f"Matches: {matches}")

    s = "aabxaabxcaabxaabxay"
    z_arr = build_z_array(s)
    print(f"\nString: '{s}'")
    print(f"Z-array: {z_arr}")

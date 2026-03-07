# ------------------------------------------------------------
# File: 29_longest_common_prefix.py
# Purpose: Longest common prefix of strings.
# Description: Vertical scan or sort and compare first/last.
# ------------------------------------------------------------

def longest_common_prefix(strs: list[str]) -> str:
    if not strs: return ""
    for i, c in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != c:
                return strs[0][:i]
    return strs[0]

def main():
    print(longest_common_prefix(["flower", "flow", "flight"]))
    print(longest_common_prefix(["dog", "racecar", "car"]))

if __name__ == "__main__":
    main()

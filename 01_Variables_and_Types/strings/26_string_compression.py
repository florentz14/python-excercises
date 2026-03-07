# ------------------------------------------------------------
# File: 26_string_compression.py
# Purpose: Run-length encoding.
# Description: "aabcccccaaa" -> "a2b1c5a3".
# ------------------------------------------------------------

def compress(s: str) -> str:
    if not s: return ""
    result, count = [], 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]: count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return "".join(result)

def main():
    print(compress("aabcccccaaa"))
    print(compress("abc"))

if __name__ == "__main__":
    main()

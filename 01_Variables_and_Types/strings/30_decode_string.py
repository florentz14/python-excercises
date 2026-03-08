# -------------------------------------------------
# File Name: 30_decode_string.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Decode encoded string. E.g. "3[a2[c]]" -> "accaccacc".
# -------------------------------------------------

def decode_string(s: str) -> str:
    stack: list[str | int] = []
    curr_str, curr_num = "", 0
    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        elif c == "[":
            stack.append(curr_str)
            stack.append(curr_num)
            curr_str, curr_num = "", 0
        elif c == "]":
            num = stack.pop()
            prev_str = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += c
    return curr_str

def main() -> None:
    s = "3[a2[c]]"
    print(decode_string(s))

if __name__ == "__main__":
    main()

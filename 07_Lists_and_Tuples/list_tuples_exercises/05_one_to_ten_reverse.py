# -------------------------------------------------
# File Name: 05_one_to_ten_reverse.py
# Description: Numbers 1-10 in reverse, comma separated
# -------------------------------------------------

nums = list(range(1, 11))
nums.reverse()
print(", ".join(str(x) for x in nums))

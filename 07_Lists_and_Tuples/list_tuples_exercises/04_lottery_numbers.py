# -------------------------------------------------
# File Name: 04_lottery_numbers.py
# Description: Lottery winning numbers, sorted ascending
# -------------------------------------------------

nums = []
for i in range(6):
    n = int(input(f"Winning number {i + 1}: "))
    nums.append(n)
nums.sort()
print("Sorted:", nums)

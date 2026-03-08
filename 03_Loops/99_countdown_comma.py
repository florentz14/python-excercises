# -------------------------------------------------
# File Name: 99_countdown_comma.py
# Description: Countdown from n to 0, comma separated
# -------------------------------------------------

n = int(input("Enter a positive integer: "))
parts = [str(i) for i in range(n, -1, -1)]
print(", ".join(parts))

# -------------------------------------------------
# File Name: 15_countdown.py
# Author: Florentino Báez
# Date: 04_Functions
# Description: Countdown from n to 1, then "Go!".
# -------------------------------------------------

def countdown(n: int) -> None:
    for i in range(n, 0, -1):
        print(i)
    print("Go!")


countdown(5)

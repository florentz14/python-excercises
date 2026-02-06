# -------------------------------------------------
# File: 15_countdown.py
# Description: Countdown from n to 1, then "Go!".
#              Function with reverse loop.
# -------------------------------------------------

def countdown(n: int) -> None:
    for i in range(n, 0, -1):
        print(i)
    print("Go!")


countdown(5)

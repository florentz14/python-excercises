# Functions with Loops - Exercise 5: Countdown

def countdown(n: int) -> None:
    for i in range(n, 0, -1):
        print(i)
    print("Go!")


countdown(5)

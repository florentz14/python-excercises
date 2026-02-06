# Functions with Loops - Exercise 3: Multiplication table

def multiplication_table(num: int) -> None:
    for i in range(1, 6):
        print(num, "x", i, "=", num * i)


multiplication_table(3)

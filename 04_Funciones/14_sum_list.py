# Functions with Loops - Exercise 4: Sum list

def sum_list(numbers: list[int | float]) -> None:
    total = 0
    for n in numbers:
        total += n
    print(total)


sum_list([2, 4, 6, 8])

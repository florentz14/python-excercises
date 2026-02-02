# 195. Traverse List in Reverse with Original Index

def reverse_with_index(lst: list) -> None:
    for i in range(len(lst) - 1, -1, -1):
        print(i, lst[i])


sample = ['red', 'green', 'white', 'black']
reverse_with_index(sample)

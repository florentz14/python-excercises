# 265. Generate Fibonacci List (first n terms)

def fibonacci_list(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


print(fibonacci_list(7))   # [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_list(15))

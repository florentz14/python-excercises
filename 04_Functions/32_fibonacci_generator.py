# -------------------------------------------------
# File: 32_fibonacci_generator.py
# Description: Fibonacci sequence generator.
#              Using yield for lazy evaluation.
# -------------------------------------------------

def fibonacci(limit):
    """
    Generates Fibonacci numbers up to the specified limit.
    
    Args:
        limit: Maximum value to generate
        
    Yields:
        Fibonacci numbers from 0 up to limit
    """
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def fibonacci_n_terms(n):
    """
    Generates the first n Fibonacci numbers.
    
    Args:
        n: Number of terms to generate
        
    Yields:
        The first n Fibonacci numbers
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# Example usage
if __name__ == "__main__":
    print("=== Fibonacci Generator Demo ===\n")
    
    # Fibonacci up to a limit
    print("Fibonacci numbers up to 100:")
    print(list(fibonacci(100)))
    print()
    
    # First N Fibonacci numbers
    print("First 15 Fibonacci numbers:")
    print(list(fibonacci_n_terms(15)))
    print()
    
    # Using the generator in a loop
    print("Fibonacci numbers up to 50 (one by one):")
    for num in fibonacci(50):
        print(num, end=" ")
    print()
    print()
    
    # Sum of Fibonacci numbers
    fib_sum = sum(fibonacci(100))
    print(f"Sum of Fibonacci numbers up to 100: {fib_sum}")

# -------------------------------------------------
# File: 40_memoize_decorator.py
# Description: Memoization decorator (caching).
#              Optimize recursive functions.
# -------------------------------------------------

def memoize(func):
    """
    Decorator that caches function results.
    
    Stores computed results in a dictionary to avoid
    recalculating the same inputs multiple times.
    
    Args:
        func: Function to be memoized
        
    Returns:
        Wrapper function with caching capability
    """
    cache = {}
    
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    # Expose cache for inspection
    wrapper.cache = cache
    return wrapper


@memoize
def expensive_calculation(n):
    """Simulates an expensive calculation - sum of squares."""
    print(f"  Computing for n={n}...")
    return sum(i ** 2 for i in range(n))


@memoize
def fibonacci(n):
    """Calculates Fibonacci number with memoization."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@memoize
def factorial(n):
    """Calculates factorial with memoization."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Example usage
if __name__ == "__main__":
    print("=== Memoization Decorator Demo ===\n")
    
    # Example 1: Expensive calculation
    print("1. Expensive calculation (sum of squares):")
    print(f"  Result: {expensive_calculation(1000)}")
    print(f"  Result (cached): {expensive_calculation(1000)}")
    print(f"  New value: {expensive_calculation(500)}")
    print(f"  Cache contents: {list(expensive_calculation.cache.keys())}")
    
    print()
    
    # Example 2: Fibonacci with memoization
    print("2. Fibonacci sequence (memoized):")
    print("  Computing fib(30)...")
    result = fibonacci(30)
    print(f"  fib(30) = {result}")
    print(f"  Cache has {len(fibonacci.cache)} entries")
    
    print()
    
    # Show some Fibonacci values
    print("  First 15 Fibonacci numbers:")
    fib_seq = [fibonacci(i) for i in range(15)]
    print(f"  {fib_seq}")
    
    print()
    
    # Example 3: Factorial with memoization
    print("3. Factorial (memoized):")
    for n in [5, 10, 7, 10, 12]:
        result = factorial(n)
        print(f"  {n}! = {result}")
    
    print()
    
    # Show cache benefit
    print("4. Performance comparison:")
    import time
    
    # Without memoization - recreate function
    def fib_slow(n):
        if n < 2:
            return n
        return fib_slow(n - 1) + fib_slow(n - 2)
    
    # Time slow version
    start = time.time()
    fib_slow(30)
    slow_time = time.time() - start
    
    # Reset memoized cache and time
    fibonacci.cache.clear()
    start = time.time()
    fibonacci(30)
    fast_time = time.time() - start
    
    print(f"  Without memoization: {slow_time:.4f} seconds")
    print(f"  With memoization:    {fast_time:.4f} seconds")
    print(f"  Speedup: {slow_time/fast_time:.0f}x faster")

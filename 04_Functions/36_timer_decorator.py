# -------------------------------------------------
# File: 36_timer_decorator.py
# Description: Timer decorator for execution time.
#              Measure function performance.
# -------------------------------------------------

import time


def timer_decorator(func):
    """
    Decorator that measures the execution time of a function.
    
    Args:
        func: Function to be decorated
        
    Returns:
        Wrapper function that times the execution
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper


def repeat_decorator(times):
    """
    Decorator that repeats a function multiple times.
    
    Args:
        times: Number of times to repeat
        
    Returns:
        Decorator function
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


# Example usage
if __name__ == "__main__":
    print("=== Timer Decorator Demo ===\n")
    
    # Function decorated with timer
    @timer_decorator
    def slow_function():
        """Simulates a slow operation"""
        time.sleep(0.3)
        return "Done!"
    
    @timer_decorator
    def calculate_sum(n):
        """Calculates sum from 1 to n"""
        total = sum(range(1, n + 1))
        return total
    
    @timer_decorator
    def find_primes(limit):
        """Finds all primes up to limit"""
        primes = []
        for num in range(2, limit + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes
    
    # Test the decorated functions
    print("1. Testing slow_function():")
    result = slow_function()
    print(f"   Result: {result}\n")
    
    print("2. Testing calculate_sum(1000000):")
    result = calculate_sum(1000000)
    print(f"   Result: {result}\n")
    
    print("3. Testing find_primes(10000):")
    result = find_primes(10000)
    print(f"   Found {len(result)} primes\n")
    
    # Repeat decorator example
    print("4. Testing repeat_decorator:")
    
    @repeat_decorator(3)
    def say_hello():
        print("   Hello!")
        return "Completed"
    
    say_hello()

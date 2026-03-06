# -------------------------------------------------
# File: 28_factorial.py
# Description: Factorial calculation using recursion.
#              Recursive function example (n!).
# -------------------------------------------------

def factorial(n):
    """
    Calculates the factorial of n using recursion.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Example usage
if __name__ == "__main__":
    print("=== Factorial Function Demo ===\n")
    
    # Test with various numbers
    for num in [0, 1, 5, 7, 10]:
        print(f"factorial({num}) = {factorial(num)}")
    
    print()
    
    # Show the calculation process for factorial(5)
    print("How factorial(5) works:")
    print("  5! = 5 * 4! = 5 * 4 * 3! = 5 * 4 * 3 * 2! = 5 * 4 * 3 * 2 * 1! = 120")
    
    # Test error handling
    print("\nTesting negative number:")
    try:
        factorial(-1)
    except ValueError as e:
        print(f"  Error: {e}")

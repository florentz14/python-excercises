# -------------------------------------------------
# File: 30_filter_even.py
# Description: Filter even/odd numbers from a list.
#              List comprehension with conditions.
# -------------------------------------------------

def filter_even(numbers):
    """
    Returns a list containing only the even numbers.
    
    Args:
        numbers: A list of integers
        
    Returns:
        A new list with only even numbers
    """
    return [num for num in numbers if num % 2 == 0]


def filter_odd(numbers):
    """
    Returns a list containing only the odd numbers.
    
    Args:
        numbers: A list of integers
        
    Returns:
        A new list with only odd numbers
    """
    return [num for num in numbers if num % 2 != 0]


# Example usage
if __name__ == "__main__":
    print("=== Filter Even/Odd Numbers Demo ===\n")
    
    # Test list
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"Original list: {numbers}")
    print(f"Even numbers:  {filter_even(numbers)}")
    print(f"Odd numbers:   {filter_odd(numbers)}")
    
    print()
    
    # Another example
    mixed = [15, 22, 33, 44, 55, 66, 77, 88]
    print(f"Mixed list:    {mixed}")
    print(f"Even numbers:  {filter_even(mixed)}")
    print(f"Odd numbers:   {filter_odd(mixed)}")

# -------------------------------------------------
# File: 33_find_primes.py
# Description: Find prime numbers in a range.
#              Prime number validation algorithm.
# -------------------------------------------------

def find_primes(start, end):
    """
    Returns a list of prime numbers between start and end (inclusive).
    
    Args:
        start: Starting number of the range
        end: Ending number of the range
        
    Returns:
        A list of prime numbers in the given range
    """
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes


def is_prime(n):
    """
    Checks if a single number is prime.
    
    Args:
        n: Number to check
        
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Example usage
if __name__ == "__main__":
    print("=== Find Prime Numbers Demo ===\n")
    
    # Find primes in different ranges
    print(f"Primes between 1-20:   {find_primes(1, 20)}")
    print(f"Primes between 10-30:  {find_primes(10, 30)}")
    print(f"Primes between 50-100: {find_primes(50, 100)}")
    print()
    
    # Check individual numbers
    print("Checking individual numbers:")
    for num in [2, 7, 15, 17, 20, 23]:
        status = "prime" if is_prime(num) else "not prime"
        print(f"  {num} is {status}")

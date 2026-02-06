# -------------------------------------------------
# File: 54_radix_sort.py
# Description: Radix Sort Algorithm.
#              Non-comparative sorting by digit position.
# -------------------------------------------------


def counting_sort_by_digit(arr, exp):
    """
    Counting sort based on digit at position exp.
    
    Args:
        arr: Array to sort
        exp: Current digit position (1, 10, 100, ...)
    
    Returns:
        Sorted array by that digit
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0-9
    
    # Count occurrences of each digit
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    
    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array (right to left for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    return output


def radix_sort(arr):
    """
    Radix Sort - sorts numbers digit by digit.
    
    Time Complexity: O(d * (n + k))
        - d = number of digits in max number
        - n = number of elements
        - k = range of digits (0-9 = 10)
    
    Space Complexity: O(n + k)
    
    Args:
        arr: Array of non-negative integers
        
    Returns:
        Sorted array
    """
    if not arr:
        return arr
    
    # Handle negative numbers separately if needed
    arr = arr.copy()
    
    # Find maximum to know number of digits
    max_val = max(arr)
    
    # Sort by each digit position
    exp = 1  # Start with least significant digit
    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10  # Move to next digit
    
    return arr


def radix_sort_with_negatives(arr):
    """
    Radix Sort that handles negative numbers.
    
    Args:
        arr: Array of integers (positive and negative)
        
    Returns:
        Sorted array
    """
    if not arr:
        return arr
    
    # Separate positive and negative numbers
    positives = [x for x in arr if x >= 0]
    negatives = [-x for x in arr if x < 0]  # Make positive for sorting
    
    # Sort both arrays
    sorted_positives = radix_sort(positives) if positives else []
    sorted_negatives = radix_sort(negatives) if negatives else []
    
    # Combine: negatives (reversed, then negated) + positives
    result = [-x for x in reversed(sorted_negatives)] + sorted_positives
    return result


def radix_sort_strings(arr, max_length=None):
    """
    Radix Sort for strings (LSD - Least Significant Digit).
    
    Args:
        arr: Array of strings
        max_length: Maximum string length (optional)
        
    Returns:
        Sorted array of strings
    """
    if not arr:
        return arr
    
    # Pad strings to same length
    if max_length is None:
        max_length = max(len(s) for s in arr)
    
    # Sort from rightmost character to leftmost
    for pos in range(max_length - 1, -1, -1):
        # Use counting sort for this position
        buckets = [[] for _ in range(256)]  # ASCII characters
        
        for s in arr:
            # Get character at position (or 0 if string is shorter)
            char_code = ord(s[pos]) if pos < len(s) else 0
            buckets[char_code].append(s)
        
        # Flatten buckets
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
    
    return arr


# Visualization helper
def visualize_radix_sort(arr):
    """Show step-by-step radix sort process."""
    print(f"Original: {arr}")
    
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1
    step = 1
    
    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        digit_name = ["ones", "tens", "hundreds", "thousands"][step - 1] if step <= 4 else f"10^{step-1}"
        print(f"Step {step} (by {digit_name}): {arr}")
        exp *= 10
        step += 1
    
    return arr


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("RADIX SORT")
    print("=" * 50)
    
    # Basic example
    print("\n1. Basic Radix Sort:")
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"   Original: {arr}")
    sorted_arr = radix_sort(arr)
    print(f"   Sorted:   {sorted_arr}")
    
    # Step-by-step visualization
    print("\n2. Step-by-step visualization:")
    arr = [329, 457, 657, 839, 436, 720, 355]
    visualize_radix_sort(arr)
    
    # With negative numbers
    print("\n3. With negative numbers:")
    arr = [170, -45, 75, -90, 802, -24, 2, 66]
    print(f"   Original: {arr}")
    sorted_arr = radix_sort_with_negatives(arr)
    print(f"   Sorted:   {sorted_arr}")
    
    # String sorting
    print("\n4. String sorting:")
    strings = ["cat", "dog", "ant", "bat", "cow", "ape"]
    print(f"   Original: {strings}")
    sorted_strings = radix_sort_strings(strings)
    print(f"   Sorted:   {sorted_strings}")
    
    # Large numbers
    print("\n5. Large numbers:")
    arr = [12345, 67890, 11111, 99999, 10000, 55555]
    print(f"   Original: {arr}")
    sorted_arr = radix_sort(arr)
    print(f"   Sorted:   {sorted_arr}")
    
    # Complexity comparison
    print("\n" + "=" * 50)
    print("COMPLEXITY ANALYSIS")
    print("=" * 50)
    print("""
    Radix Sort:
    - Time:  O(d * (n + k)) where d = digits, k = base (10)
    - Space: O(n + k)
    - Stable: Yes
    - Best for: Large arrays of integers with limited digit count
    
    Comparison with other sorts:
    - Better than O(n log n) when d < log n
    - Not comparison-based (breaks O(n log n) lower bound)
    - Works best with fixed-length keys
    """)

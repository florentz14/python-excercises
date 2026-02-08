# -------------------------------------------------
# File Name: 26_performance.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Dictionary Performance and Best Practices.
#              Benchmarks dict vs list lookups, memory usage,
#              comprehension vs loop speed, and membership tests.
#              Covers valid key types, merging techniques (3.9+),
#              common pitfalls, and a best-practices summary.
# -------------------------------------------------

"""
Exercise 10: Dictionary Performance and Best Practices
This exercise explores dictionary performance characteristics and optimization techniques.
Learn when and how to use dictionaries efficiently.
"""

import time
import sys
from collections import defaultdict


def measure_time(func):
    """Decorator to measure function execution time."""
    def wrapper(*args, **kwargs):
        # Record start time
        start = time.time()
        result = func(*args, **kwargs)
        # Calculate elapsed time in milliseconds
        end = time.time()
        print(f"  Execution time: {(end - start) * 1000:.4f} ms")
        return result
    return wrapper


def main():
    print("Exercise 10: Dictionary Performance & Best Practices")
    print("=" * 60)
    
    # 1. Dictionary vs List lookup performance comparison
    print("\n1. Lookup Performance: Dictionary vs List")
    print("-" * 60)
    
    # Create test data structures of equal size
    size = 10000
    # Dictionary with integer keys
    test_dict = {i: f"value_{i}" for i in range(size)}
    # List of tuples (simulating key-value pairs)
    test_list = [(i, f"value_{i}") for i in range(size)]
    # Search for last item - worst case for list (O(n))
    search_key = size - 1
    
    # Dictionary lookup: O(1) average case
    @measure_time
    def dict_lookup():
        for _ in range(1000):
            _ = test_dict.get(search_key)
    
    # List lookup: O(n) - must iterate through list
    @measure_time
    def list_lookup():
        for _ in range(1000):
            _ = next((v for k, v in test_list if k == search_key), None)
    
    print(f"Searching for key {search_key} 1000 times in {size} items:")
    print("Dictionary lookup:")
    dict_lookup()
    print("List lookup:")
    list_lookup()
    print("Result: Dictionary is O(1), List is O(n) - MUCH faster!")
    print()
    
    # 2. Memory usage analysis
    print("2. Memory Usage Comparison:")
    print("-" * 60)
    
    # Create dictionaries of different sizes
    small_dict = {i: i for i in range(100)}
    large_dict = {i: i for i in range(10000)}
    
    # Display memory usage statistics
    print(f"Small dict (100 items): {sys.getsizeof(small_dict)} bytes")
    print(f"Large dict (10,000 items): {sys.getsizeof(large_dict)} bytes")
    # Calculate approximate per-item overhead
    print(f"Per-item overhead: ~{sys.getsizeof(large_dict) / 10000:.2f} bytes")
    print("Note: Dictionaries use more memory than lists for space/speed tradeoff")
    print()
    
    # 3. Valid and invalid dictionary key types
    print("3. Valid and Invalid Dictionary Keys:")
    print("-" * 60)
    
    # Examples of valid keys (must be hashable/immutable)
    valid_keys = {
        42: "integer key",
        "hello": "string key",
        (1, 2, 3): "tuple key",  # Tuples are immutable
        3.14: "float key",
        True: "boolean key"
    }
    print("✓ Valid keys (hashable/immutable):")
    for key in valid_keys.keys():
        print(f"  {type(key).__name__}: {key}")
    print()
    
    # Examples of invalid keys (mutable types)
    print("✗ Invalid keys (not hashable):")
    try:
        # Lists are mutable - cannot be used as keys
        invalid = {[1, 2, 3]: "list key"}
    except TypeError as e:
        print(f"  List: TypeError - {e}")
    
    try:
        # Dictionaries are mutable - cannot be used as keys
        invalid = {{"a": 1}: "dict key"}
    except TypeError as e:
        print(f"  Dict: TypeError - {e}")
    print()
    
    # 4. Dictionary comprehension vs traditional loop performance
    print("4. Performance: Comprehension vs Loop:")
    print("-" * 60)
    
    # Traditional loop approach
    @measure_time
    def using_loop():
        result = {}
        for i in range(10000):
            result[i] = i ** 2
        return result
    
    # Dictionary comprehension approach (typically faster)
    @measure_time
    def using_comprehension():
        return {i: i ** 2 for i in range(10000)}
    
    print("Creating 10,000 item dictionary:")
    print("Using loop:")
    using_loop()
    print("Using comprehension:")
    using_comprehension()
    print("Result: Comprehension is typically faster!")
    print()
    
    # 5. Safe dictionary access methods
    print("5. Safe Access: get() vs Direct []:")
    print("-" * 60)
    
    data = {"a": 1, "b": 2, "c": 3}
    
    # Direct access with [] operator - raises KeyError if missing
    print("Direct access with []:")
    try:
        value = data["missing"]
    except KeyError:
        print("  ✗ KeyError raised for missing key")
    
    # Safe access with get() - returns default value if missing
    print("Safe access with get():")
    value = data.get("missing", "default")
    print(f"  ✓ Returns: {value}")
    
    print("\nBest Practice: Use get() when key might not exist")
    print()
    
    # 6. Efficient dictionary update methods
    print("6. Efficient Dictionary Updates:")
    print("-" * 60)
    
    # Individual updates in a loop
    @measure_time
    def update_individually():
        d = {}
        for i in range(1000):
            d[f"key_{i}"] = i
    
    # Batch update using update() method
    @measure_time
    def update_batch():
        d = {}
        d.update({f"key_{i}": i for i in range(1000)})
    
    print("Adding 1000 items individually:")
    update_individually()
    print("Adding 1000 items with update():")
    update_batch()
    print()
    
    # 7. Membership testing performance comparison
    print("7. Membership Testing:")
    print("-" * 60)
    
    # Create large dictionary for testing
    large_dict = {i: i for i in range(100000)}
    
    # Direct membership test - O(1) average case
    @measure_time
    def check_in_dict():
        for _ in range(10000):
            _ = 99999 in large_dict
    
    # Membership test via keys() view - also O(1) but slightly slower
    @measure_time
    def check_in_keys():
        for _ in range(10000):
            _ = 99999 in large_dict.keys()
    
    print("Checking membership 10,000 times:")
    print("Using 'in dict':")
    check_in_dict()
    print("Using 'in dict.keys()':")
    check_in_keys()
    print("Result: Both are O(1), but 'in dict' is slightly faster")
    print()
    
    # 8. Dictionary merging techniques (Python 3.9+)
    print("8. Dictionary Merging (Python 3.9+):")
    print("-" * 60)
    
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    dict3 = {"b": 20, "e": 5}  # Has conflicting key 'b'
    
    # Method 1: Using update() method (modifies in place)
    merged1 = dict1.copy()
    merged1.update(dict2)
    print(f"Using update(): {merged1}")
    
    # Method 2: Using ** unpacking operator
    merged2 = {**dict1, **dict2}
    print(f"Using ** unpacking: {merged2}")
    
    # Method 3: Using | operator (Python 3.9+)
    merged3 = dict1 | dict2
    print(f"Using | operator: {merged3}")
    
    # Handling key conflicts - rightmost dict wins
    merged_conflict = dict1 | dict3
    print(f"With conflicts (dict3 wins): {merged_conflict}")
    print()
    
    # 9. Common pitfalls and how to avoid them
    print("9. Common Pitfalls to Avoid:")
    print("-" * 60)
    
    # Pitfall 1: Modifying dictionary during iteration
    print("Pitfall 1: Modifying during iteration")
    test_dict = {"a": 1, "b": 2, "c": 3}
    print("✗ BAD: Modifying dict while iterating")
    print("  # for key in dict: del dict[key]  # RuntimeError!")
    print("✓ GOOD: Use list() to copy keys first")
    # Create list copy of keys to safely modify during iteration
    for key in list(test_dict.keys()):
        if test_dict[key] == 2:
            del test_dict[key]
    print(f"  Result: {test_dict}")
    print()
    
    # Pitfall 2: Mutable default arguments
    print("Pitfall 2: Mutable default values")
    print("✗ BAD: Using {} as default parameter")
    print("  def func(d={})  # Same dict reused!")
    print("✓ GOOD: Use None and create new dict")
    print("  def func(d=None): d = d or {}")
    print()
    
    # Pitfall 3: Shallow copy vs deep copy
    print("Pitfall 3: Shallow vs Deep copy")
    original = {"a": [1, 2, 3], "b": [4, 5, 6]}
    # copy() creates shallow copy - nested objects are still referenced
    shallow = original.copy()
    shallow["a"].append(99)
    print(f"Original after shallow copy modification: {original}")
    print("Note: Nested objects are still referenced!")
    print()
    
    # 10. Best practices summary
    print("10. Best Practices Summary:")
    print("-" * 60)
    
    # Dictionary of best practices organized by topic
    best_practices = {
        "Lookups": "Use dicts for O(1) lookups vs lists O(n)",
        "Keys": "Only use immutable/hashable types as keys",
        "Access": "Use .get() for safe access with defaults",
        "Existence": "Use 'in' for membership testing",
        "Iteration": "Don't modify dict during iteration",
        "Comprehension": "Prefer dict comprehensions for readability",
        "Merging": "Use | operator (3.9+) or ** unpacking",
        "Defaults": "Use defaultdict for auto-initialization",
        "Memory": "Dicts use more memory for faster access",
        "Type hints": "Use dict[str, int] for better code clarity"
    }
    
    # Display all best practices
    print("Key recommendations:")
    for topic, tip in best_practices.items():
        print(f"  {topic:15} → {tip}")
    
    print("\n" + "=" * 60)
    print("Performance Tips:")
    print("  ✓ Dictionaries are optimized for fast lookups")
    print("  ✓ Use dict comprehensions when possible")
    print("  ✓ Use get() method to avoid KeyError")
    print("  ✓ Use defaultdict for counting/grouping")
    print("  ✓ Only use immutable keys")
    print("  ✓ Be careful with shallow copies of nested dicts")


if __name__ == "__main__":
    main()

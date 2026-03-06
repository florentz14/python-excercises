# ------------------------------------------------------------
# Algorithm: Frequency Count with Hash Map
# Purpose:
#   Count how many times each element appears in a list.
#   Core pattern for: duplicates, top K, grouping, anagrams.
# Complexity:
#   Time  : O(n)
#   Space : O(n)
# ------------------------------------------------------------
# Author: Florentino Báez
# ------------------------------------------------------------


def frequency_count(items: list) -> dict:
    """
    Count frequency of each item. Works with str, int, hashable types.
    """
    # Store frequency of each item
    counts = {}

    for item in items:
        # Increase count using dict.get for concise handling
        counts[item] = counts.get(item, 0) + 1

    return counts


if __name__ == "__main__":
    print("=== Hash Map: Frequency Count ===\n")

    examples = [
        ["apple", "banana", "apple", "cherry", "banana", "apple"],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
    ]
    for items in examples:
        print(f"Input: {items}")
        print(f"  Frequencies: {frequency_count(items)}")

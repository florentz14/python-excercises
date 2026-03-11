# -------------------------------------------------
# File Name: 35_linear_search.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Linear search. Sequential traversal; works with unsorted lists. O(n).
# -------------------------------------------------

def linear_search(items, target):
    """Search item by item. Returns index or -1."""
    for index, element in enumerate(items):
        if element == target:
            return index  # Found -> return position
    return -1  # Not found


def linear_search_sorted(items, target):
    """If list is sorted, stop when current element exceeds target."""
    for index, element in enumerate(items):
        if element == target:
            return index
        if items[index] > target:
            return -1  # In sorted list, it cannot be further ahead
    return -1


def linear_search_all(items, target):
    """Return all indices where target appears."""
    indices = []
    for index, element in enumerate(items):
        if element == target:
            indices.append(index)  # Store each position found
    return indices


if __name__ == "__main__":
    sample = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print("List:", sample)
    print("Linear search for 5:", linear_search(sample, 5))
    print("All occurrences of 5:", linear_search_all(sample, 5))


# Backward-compatible aliases.
busqueda_lineal = linear_search
busqueda_lineal_optimizada = linear_search_sorted
busqueda_lineal_todas = linear_search_all

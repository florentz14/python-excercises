# -------------------------------------------------
# File: 01_mochila_fraccionaria.py (Fractional Knapsack)
# -------------------------------------------------
# Author: Florentino Báez
# Module: Data Structures - Greedy Algorithms
#
# Description:
#   Solves the Fractional Knapsack Problem using a greedy strategy.
#   Items can be taken partially (fractionally). The algorithm sorts
#   items by value/weight ratio and always picks the item with highest
#   ratio first until the knapsack is full.
#
# Strategy: Take items with highest value/weight ratio first.
# Complexity: O(n log n) due to sorting.
# -------------------------------------------------


def fractional_knapsack(weights, values, capacity):
    """
    Solves the fractional knapsack problem using a greedy algorithm.
    Returns: (total_value, solution_list) where solution_list contains
    (item_index, fraction_taken) tuples.
    """
    n = len(weights)
    # Build list of (value/weight ratio, weight, value, index) for sorting
    items = [(values[i] / weights[i], weights[i], values[i], i) for i in range(n)]
    # Sort by ratio descending: greedy = take highest value-per-unit-weight first
    items.sort(reverse=True)

    total_value = 0
    current_weight = 0
    solution = []  # List of (index, fraction) for each selected item

    for ratio, w, val, idx in items:
        if current_weight + w <= capacity:
            # Entire item fits; take it completely
            current_weight += w
            total_value += val
            solution.append((idx, 1.0))
        else:
            # Only a fraction fits; take what we can and stop
            fraction = (capacity - current_weight) / w
            current_weight = capacity
            total_value += val * fraction
            solution.append((idx, fraction))
            break  # Knapsack is full

    return total_value, solution


if __name__ == "__main__":
    print("=== Greedy Algorithms: Fractional Knapsack ===\n")

    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")

    total_val, solution = fractional_knapsack(weights, values, capacity)
    print(f"\nMaximum value: {total_val}")
    print("Solution (index, fraction):")
    for idx, frac in solution:
        print(f"  Item {idx}: {frac*100:.1f}% (weight: {weights[idx]*frac:.1f}, value: {values[idx]*frac:.1f})")

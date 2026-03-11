# -------------------------------------------------
# File Name: 43_sort_utilities.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Sort utilities. Common helpers for sorting algorithms.
# -------------------------------------------------

import random


def is_sorted(items):
    """Checks if a list is sorted in ascending order."""
    return all(items[i] <= items[i + 1] for i in range(len(items) - 1))


def generate_random_list(n, minimum=1, maximum=100):
    """Generates a random list of n elements."""
    return [random.randint(minimum, maximum) for _ in range(n)]


if __name__ == "__main__":
    items = generate_random_list(5, 1, 20)
    print("Random list:", items)
    print("Is sorted?", is_sorted(items))
    print("Is [1,2,3] sorted?", is_sorted([1, 2, 3]))


# Backward-compatible aliases.
esta_ordenada = is_sorted
generar_lista_aleatoria = generate_random_list

# -------------------------------------------------
# File Name: 08_sort_tuples_by_last_element.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Demonstrates sort tuples by last element.
# -------------------------------------------------

def sort_by_last(tuples: list[tuple]) -> list[tuple]:
    # sorted() crea una lista ordenada sin modificar la original
    # key=lambda t: t[-1] indica que el criterio de orden es el último elemento
    return sorted(tuples, key=lambda t: t[-1])


# --- Ejemplo: [(2,5), (1,2), (4,4), (2,3), (2,1)] -> orden por 5,2,4,3,1
sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_by_last(sample))  # [(2,1), (1,2), (2,3), (4,4), (2,5)]

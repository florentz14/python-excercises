# -------------------------------------------------
# File Name: 47_merge.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Merge Sort.
#              Recursively divides the list in half until
#              sublists of one element, then merges them
#              in order. Divide and conquer paradigm.
#              Guarantees O(n log n) in all cases.
#              Complexity: O(n log n). Stable. Space O(n).
# -------------------------------------------------


def merge_sort(lista):
    """Divide and conquer: divide, sort halves, merge."""
    if len(lista) <= 1:
        return lista.copy()  # Base case: list of 0-1 elements
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])   # Sort left half
    derecha = merge_sort(lista[medio:])     # Sort right half
    return merge(izquierda, derecha)        # Merge both halves


def merge(izquierda, derecha):
    """Merges two sorted lists into one sorted list."""
    resultado = []
    i = j = 0
    # Compare and take the smaller from each list
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    # Append remaining elements
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Merge Sort:", merge_sort(ejemplo))

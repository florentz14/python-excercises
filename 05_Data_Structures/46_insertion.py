# -------------------------------------------------
# File Name: 46_insertion.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Insertion Sort. Builds sorted prefix by inserting each element. O(n²). Stable.
# -------------------------------------------------

def insertion_sort(lista):
    """Inserts each element into its place within the already sorted portion."""
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]  # Element to insert
        j = i - 1
        # Shift elements greater than key to the right
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave  # Insert key at its correct position
    return lista


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", arr)
    print("Insertion Sort:", insertion_sort(arr))

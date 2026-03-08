# -------------------------------------------------
# File Name: 50_counting.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Counting Sort. Non-comparison sort for small integer range. O(n+k).
# -------------------------------------------------

def counting_sort(lista, maximo=None):
    """Sorts by counting occurrences of each value (non-negative integers)."""
    if maximo is None:
        maximo = max(lista) if lista else 0
    count = [0] * (maximo + 1)  # Count array for each possible value
    for num in lista:
        count[num] += 1         # Count each occurrence
    resultado = []
    for i in range(maximo + 1):
        resultado.extend([i] * count[i])  # Rebuild sorted list
    return resultado


if __name__ == "__main__":
    ejemplo = [4, 2, 2, 8, 3, 3, 1]
    print("Lista original:", ejemplo)
    print("Counting Sort:", counting_sort(ejemplo))

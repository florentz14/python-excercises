# ------------------------------------------------------------
# Program: Binary Search (Fundamentals)
# Purpose:
#   Search for a target value inside a sorted array.
#
# Requirements:
#   The array must be sorted in ascending order.
#
# Method:
#   Repeatedly divide the search space in half.
#
# Complexity:
#   Time  : O(log n)
#   Space : O(1)
#
# Comparison:
#   | Linear Search | O(n)     |
#   | Binary Search | O(log n) |
#
#   Example with 1,000,000 elements:
#   - Linear: ~1,000,000 steps
#   - Binary: ~20 steps
# ------------------------------------------------------------


def binary_search_classic(arr: list[int], target: int) -> int:
    """
    Versión clásica. Usa mid = (left + right) // 2.
    Returns index of target, or -1 if not found.
    """
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_optimized(arr: list[int], target: int) -> int:
    """
    Versión optimizada y segura.
    Usa mid = left + (right - left) // 2 para evitar overflow
    en lenguajes como C++/Java. Preferida en entrevistas técnicas.

    Returns index of target, or -1 if not found.
    """
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Safer middle calculation

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search(arr: list[int], target: int, optimized: bool = True) -> int:
    """
    Wrapper que usa la versión optimizada por defecto.
    """
    return binary_search_optimized(arr, target) if optimized else binary_search_classic(arr, target)


# ------------------------------------------------------------
# Regla de oro: Binary Search solo funciona si el arreglo está ordenado.
# Si no está ordenado: sort(arr) primero (cuesta O(n log n)).
# ------------------------------------------------------------


if __name__ == "__main__":
    # Ejemplo básico
    arr = [1, 3, 5, 7, 9, 11, 15]
    target = 7
    result = binary_search_optimized(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target} -> Index: {result}")

    # Buscar 11: Paso 1 mid=7 (target>7) -> derecha; Paso 2 mid=11 found
    target2 = 11
    result2 = binary_search_optimized(arr, target2)
    print(f"Target: {target2} -> Index: {result2}")

    # No encontrado
    target3 = 8
    result3 = binary_search_optimized(arr, target3)
    print(f"Target: {target3} -> Index: {result3} (not found)")

    # Versión con entrada de usuario (descomentar para usar)
    # arr = [int(x) for x in input().split()]
    # target = int(input())
    # print(binary_search(arr, target))

# ------------------------------------------------------------
# Program: Binary Search - 6 Variantes de Entrevista
# Purpose: Las variantes más importantes en entrevistas técnicas.
#
# Orden de estudio recomendado:
#   1. binary_search (normal)
#   2. first_occurrence
#   3. last_occurrence
#   4. search_insert_position
#   5. search_rotated_sorted
#   6. find_peak (peak_element)
#
# Resumen mental:
#   - ¿Arreglo ordenado? Si no, quizá no se puede usar directamente.
#   - ¿Cualquier posición? -> binary_search normal
#   - ¿Primera/última aparición? -> guarda respuesta y sigue buscando
#   - ¿Dónde insertar? -> devuelve left al final
#   - ¿Propiedad especial (pico, rotado)? -> variante específica
#
# Tabla resumen:
#   | Problema               | Resultado                      |
#   | Standard Binary Search | índice exacto                  |
#   | First Occurrence       | primera posición               |
#   | Last Occurrence        | última posición                |
#   | Search Insert Position | índice o posición de inserción |
#   | Peak Element           | índice de un pico              |
#   | Rotated Sorted Array   | índice en arreglo rotado       |
#
# Complexity: O(log n) tiempo, O(1) espacio en todos.
# ------------------------------------------------------------


def binary_search(arr: list[int], target: int) -> int:
    """
    1. Standard Binary Search
    Find the index of the target in a sorted array.
    Return -1 if not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def first_occurrence(arr: list[int], target: int) -> int:
    """
    2. First Occurrence
    Si el número aparece varias veces, devolver la PRIMERA posición.
    Ej: [1,2,2,2,3,4], target=2 -> 1
    Idea: Cuando encuentras el target, sigue buscando hacia la izquierda.
    """
    left, right = 0, len(arr) - 1
    answer = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            answer = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer


def last_occurrence(arr: list[int], target: int) -> int:
    """
    3. Last Occurrence
    Si el número aparece varias veces, devolver la ÚLTIMA posición.
    Ej: [1,2,2,2,3,4], target=2 -> 3
    Idea: Cuando encuentras el target, sigue buscando hacia la derecha.
    """
    left, right = 0, len(arr) - 1
    answer = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            answer = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer


def search_insert_position(arr: list[int], target: int) -> int:
    """
    4. Search Insert Position
    Si el número existe, devolver su índice.
    Si no existe, devolver la posición donde debería insertarse.
    Ej: [1,3,5,6], target=5->2, target=2->1, target=7->4
    Idea: Si no se encuentra, left es la posición de inserción correcta.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


def find_peak(arr: list[int]) -> int:
    """
    5. Find Peak Element
    Encontrar un elemento mayor que sus vecinos: arr[i] > arr[i-1] y arr[i] > arr[i+1]
    Ej: [1,3,20,4,1,0] -> 2 (porque 20 > 3 y 20 > 4)
    Idea: Si arr[mid] < arr[mid+1], hay subida -> pico a la derecha.
          Si no, pico a la izquierda (incluyendo mid).
    """
    if not arr:
        return -1
    if len(arr) == 1:
        return 0

    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


# Alias para consistencia con nombres previos
peak_element = find_peak


def search_rotated_sorted(arr: list[int], target: int) -> int:
    """
    6. Search in Rotated Sorted Array
    Arreglo ordenado rotado: [4,5,6,7,0,1,2]
    En cada paso, una mitad siempre está ordenada. Descubrir cuál y decidir.
    """
    if not arr:
        return -1

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# ------------------------------------------------------------
# Ejemplos de uso - Orden de estudio
# ------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 55)
    print("1. Standard Binary Search")
    print("=" * 55)
    arr = [1, 3, 5, 7, 9, 11]
    print(f"Array: {arr}")
    print(f"Target 7 -> index {binary_search(arr, 7)}")
    print(f"Target 8 -> index {binary_search(arr, 8)} (not found)")

    print("\n" + "=" * 55)
    print("2. First / 3. Last Occurrence")
    print("=" * 55)
    arr1 = [1, 2, 2, 2, 3, 4]
    print(f"Array: {arr1}")
    print(f"First occurrence of 2: {first_occurrence(arr1, 2)}")
    print(f"Last occurrence of 2:  {last_occurrence(arr1, 2)}")

    print("\n" + "=" * 55)
    print("4. Search Insert Position")
    print("=" * 55)
    arr2 = [1, 3, 5, 6]
    for t in [5, 2, 7, 0]:
        print(f"  Target {t} -> index {search_insert_position(arr2, t)}")

    print("\n" + "=" * 55)
    print("5. Find Peak Element")
    print("=" * 55)
    arr3 = [1, 3, 20, 4, 1, 0]
    idx = find_peak(arr3)
    print(f"Array: {arr3}")
    print(f"Peak at index {idx}, value {arr3[idx]} (20 > 3 and 20 > 4)")

    print("\n" + "=" * 55)
    print("6. Search in Rotated Sorted Array")
    print("=" * 55)
    arr4 = [4, 5, 6, 7, 0, 1, 2]
    print(f"Array (rotated): {arr4}")
    for t in [0, 3, 5]:
        r = search_rotated_sorted(arr4, t)
        print(f"  Target {t} -> index {r}")

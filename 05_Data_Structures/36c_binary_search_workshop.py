# ------------------------------------------------------------
# Mini Taller: 10 Ejercicios de Binary Search
# Nivel: Fácil → Entrevista técnica
#
# Cada ejercicio incluye:
#   - Enunciado
#   - Ejemplo
#   - Solución con explicación
#   - Complejidad
#
# Ejecutar: python 36c_binary_search_workshop.py
# ------------------------------------------------------------


# =============================================================================
# NIVEL 1 - FÁCIL (Ejercicios 1-4)
# =============================================================================

def ej1_binary_search(arr: list[int], target: int) -> int:
    """
    EJERCICIO 1: Binary Search básico
    Encontrar el índice de target en un arreglo ordenado. Retornar -1 si no existe.
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


def ej2_first_occurrence(arr: list[int], target: int) -> int:
    """
    EJERCICIO 2: Primera ocurrencia
    [1,2,2,2,3], target=2 → 1
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


def ej3_last_occurrence(arr: list[int], target: int) -> int:
    """
    EJERCICIO 3: Última ocurrencia
    [1,2,2,2,3], target=2 → 3
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


def ej4_search_insert(arr: list[int], target: int) -> int:
    """
    EJERCICIO 4: Search Insert Position
    [1,3,5,6], target=5→2, target=2→1, target=7→4
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
    return left


# =============================================================================
# NIVEL 2 - MEDIO (Ejercicios 5-7)
# =============================================================================

def ej5_sqrt(x: int) -> int:
    """
    EJERCICIO 5: Square Root (Binary Search on Answer)
    Calcular floor(sqrt(x)). Ej: x=8 → 2, x=4 → 2
    Idea: Buscar el mayor entero k tal que k² <= x.
    """
    if x < 2:
        return x
    left, right = 2, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        sq = mid * mid
        if sq == x:
            return mid
        if sq < x:
            left = mid + 1
        else:
            right = mid - 1
    return right  # right es el mayor con right² < x


def ej6_guess_number(n: int, pick: int) -> int:
    """
    EJERCICIO 6: Guess Number Higher or Lower (LeetCode 374)
    Adivinar un número en [1..n]. La API 'guess' retorna: -1 (muy bajo), 0 (correcto), 1 (muy alto).
    """
    def guess(num: int) -> int:
        if num < pick:
            return 1
        if num > pick:
            return -1
        return 0

    left, right = 1, n
    while left <= right:
        mid = left + (right - left) // 2
        g = guess(mid)
        if g == 0:
            return mid
        if g == 1:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def ej7_search_rotated(arr: list[int], target: int) -> int:
    """
    EJERCICIO 7: Search in Rotated Sorted Array
    [4,5,6,7,0,1,2], target=0 → 4
    """
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


# =============================================================================
# NIVEL 3 - MEDIO-ALTO (Ejercicios 8-9)
# =============================================================================

def ej8_find_peak(arr: list[int]) -> int:
    """
    EJERCICIO 8: Find Peak Element
    [1,3,20,4,1] → 2 (20 es pico)
    """
    if len(arr) <= 1:
        return 0
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


def ej9_first_bad_version(n: int, bad: int) -> int:
    """
    EJERCICIO 9: First Bad Version (LeetCode 278)
    Versiones 1..n. is_bad(v) es True si v>=bad. Encontrar la primera mala.
    Ej: n=5, bad=4 → 4
    """
    def is_bad_version(v: int) -> bool:
        return v >= bad

    left, right = 1, n
    answer = n
    while left <= right:
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


# =============================================================================
# NIVEL 4 - ENTREVISTA (Ejercicio 10)
# =============================================================================

def ej10_min_in_rotated_sorted(arr: list[int]) -> int:
    """
    EJERCICIO 10: Find Minimum in Rotated Sorted Array (LeetCode 153)
    [4,5,6,7,0,1,2] → 0 (índice 4)
    Retornar el VALOR mínimo (no el índice). Arreglo sin duplicados.
    Idea: El mínimo está a la izquierda del "pivot". Comparar mid con right.
    """
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return arr[left]


def ej11_find_boundary(arr: list[bool]) -> int:
    """
    EJERCICIO 11: Find First True (Boundary)
    [False, False, True, True] -> 2
    Binary search on boolean list. Input: space-separated "true"/"false".
    """
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index


# =============================================================================
# EJECUCIÓN Y VERIFICACIÓN
# =============================================================================

def run_workshop():
    print("=" * 60)
    print("MINI TALLER: 10 Ejercicios de Binary Search")
    print("=" * 60)

    # Ej 1
    print("\n[1] Binary Search: arr=[1,3,5,7,9], target=7")
    print(f"    -> {ej1_binary_search([1, 3, 5, 7, 9], 7)} (esperado: 3)")

    # Ej 2
    print("\n[2] First Occurrence: [1,2,2,2,3], target=2")
    print(f"    -> {ej2_first_occurrence([1, 2, 2, 2, 3], 2)} (esperado: 1)")

    # Ej 3
    print("\n[3] Last Occurrence: [1,2,2,2,3], target=2")
    print(f"    -> {ej3_last_occurrence([1, 2, 2, 2, 3], 2)} (esperado: 3)")

    # Ej 4
    print("\n[4] Search Insert: [1,3,5,6], targets 5,2,7")
    arr4 = [1, 3, 5, 6]
    for t in [5, 2, 7]:
        print(f"    target={t} -> {ej4_search_insert(arr4, t)}")

    # Ej 5
    print("\n[5] Sqrt(8), Sqrt(4)")
    print(f"    -> sqrt(8)={ej5_sqrt(8)}, sqrt(4)={ej5_sqrt(4)} (esperado: 2, 2)")

    # Ej 6
    print("\n[6] Guess Number: n=10, pick=6")
    print(f"    -> {ej6_guess_number(10, 6)} (esperado: 6)")

    # Ej 7
    print("\n[7] Search Rotated: [4,5,6,7,0,1,2], target=0")
    print(f"    -> {ej7_search_rotated([4, 5, 6, 7, 0, 1, 2], 0)} (esperado: 4)")

    # Ej 8
    print("\n[8] Find Peak: [1,3,20,4,1]")
    arr8 = [1, 3, 20, 4, 1]
    idx8 = ej8_find_peak(arr8)
    print(f"    -> index {idx8}, value {arr8[idx8]} (esperado: 2, 20)")

    # Ej 9
    print("\n[9] First Bad Version: n=5, bad=4")
    print(f"    -> {ej9_first_bad_version(5, 4)} (esperado: 4)")

    # Ej 10
    print("\n[10] Min in Rotated: [4,5,6,7,0,1,2]")
    print(f"    -> {ej10_min_in_rotated_sorted([4, 5, 6, 7, 0, 1, 2])} (esperado: 0)")

    # Ej 11
    print("\n[11] Find First True: [False,False,True,True,True]")
    print(f"    -> {ej11_find_boundary([False, False, True, True, True])} (esperado: 2)")

    print("\n" + "=" * 60)
    print("Taller completado. Todos O(log n).")
    print("=" * 60)


if __name__ == "__main__":
    run_workshop()

# -------------------------------------------------
# File Name: 51_comparacion.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Comparison of All Sorting Methods.
#              Measures execution times of 15 algorithms on
#              the same list: Bubble, Selection, Insertion, Merge,
#              Quick, Heap, Counting, Radix, Shell, Bucket, Tim,
#              Cocktail and Comb Sort. Compares small, medium and
#              large lists showing the fastest one.
# -------------------------------------------------

import time
import random
import math


# === Utilities ===
def esta_ordenada(lista):
    """Checks if a list is sorted in ascending order."""
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def generar_lista_aleatoria(n, minimo=1, maximo=100):
    """Generates a random list of n elements."""
    return [random.randint(minimo, maximo) for _ in range(n)]


# === Bubble Sort ===
def bubble_sort(lista):
    """Classic bubble sort. Does not modify the original list."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def bubble_sort_optimizado(lista):
    """Stops if no swaps occur (list already sorted)."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
    return lista


# === Selection Sort ===
def selection_sort(lista):
    """At each step places the minimum of the rest at the current position."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


# === Insertion Sort ===
def insertion_sort(lista):
    """Inserts each element into its place within the already sorted portion."""
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


# === Merge Sort ===
def merge(izquierda, derecha):
    """Merges two sorted lists into one sorted list."""
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def merge_sort(lista):
    """Divide and conquer: divide, sort halves, merge."""
    if len(lista) <= 1:
        return lista.copy()
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)


# === Quick Sort ===
def quick_sort(lista):
    """Version that uses auxiliary lists (clear). Pivot: middle element."""
    if len(lista) <= 1:
        return lista.copy()
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)


# === Heap Sort ===
def heapify(lista, n, i):
    """Adjusts the tree so that the root at i is a max-heap."""
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2
    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda
    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)


def heap_sort(lista):
    """Builds max heap and repeatedly extracts the maximum."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)
    return lista


# === Counting Sort ===
def counting_sort(lista, maximo=None):
    """Sorts by counting occurrences of each value (non-negative integers)."""
    if not lista:
        return []
    if maximo is None:
        maximo = max(lista) if lista else 0
    count = [0] * (maximo + 1)
    for num in lista:
        count[num] += 1
    resultado = []
    for i in range(maximo + 1):
        resultado.extend([i] * count[i])
    return resultado


# === Radix Sort ===
def counting_sort_by_digit(arr, exp):
    """Counting sort by digit at position exp."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for num in arr:
        idx = (num // exp) % 10
        count[idx] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        idx = (arr[i] // exp) % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1
    return output


def radix_sort(lista):
    """Radix Sort (LSD): sorts digit by digit from least significant."""
    if not lista:
        return []
    lista = lista.copy()
    max_val = max(lista)
    exp = 1
    while max_val // exp > 0:
        lista = counting_sort_by_digit(lista, exp)
        exp *= 10
    return lista


# === Shell Sort ===
def shell_sort(lista):
    """Shell Sort with Knuth gap sequence."""
    lista = lista.copy()
    n = len(lista)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 3
    return lista


# === Bucket Sort ===
def bucket_sort(lista):
    """Bucket Sort for integers with arbitrary range."""
    if len(lista) <= 1:
        return lista.copy()
    lista = lista.copy()
    min_val = min(lista)
    max_val = max(lista)
    if min_val == max_val:
        return lista
    n = len(lista)
    num_buckets = max(1, int(math.sqrt(n)))
    rango = max_val - min_val + 1
    buckets = [[] for _ in range(num_buckets)]
    for num in lista:
        idx = int((num - min_val) / rango * num_buckets)
        if idx == num_buckets:
            idx = num_buckets - 1
        buckets[idx].append(num)
    for bucket in buckets:
        bucket.sort()
    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)
    return resultado


# === Tim Sort (simplified) ===
MIN_MERGE = 32


def _calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def _insertion_sort_range(arr, left, right):
    for i in range(left + 1, right + 1):
        clave = arr[i]
        j = i - 1
        while j >= left and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave


def _merge_runs(arr, left, mid, right):
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def tim_sort(lista):
    """Tim Sort: hybrid of Merge Sort + Insertion Sort."""
    arr = lista.copy()
    n = len(arr)
    if n <= 1:
        return arr
    min_run = _calc_min_run(n)
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        _insertion_sort_range(arr, start, end)
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                _merge_runs(arr, left, mid, right)
        size *= 2
    return arr


# === Cocktail Sort ===
def cocktail_sort(lista):
    """Cocktail Sort: bidirectional Bubble Sort."""
    lista = lista.copy()
    n = len(lista)
    inicio = 0
    fin = n - 1
    intercambiado = True
    while intercambiado:
        intercambiado = False
        for i in range(inicio, fin):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambiado = True
        fin -= 1
        if not intercambiado:
            break
        intercambiado = False
        for i in range(fin, inicio, -1):
            if lista[i] < lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                intercambiado = True
        inicio += 1
    return lista


# === Comb Sort ===
def comb_sort(lista):
    """Comb Sort: Bubble Sort with decreasing gaps (factor 1.3)."""
    lista = lista.copy()
    n = len(lista)
    gap = n
    factor = 1.3
    intercambiado = True
    while gap > 1 or intercambiado:
        gap = max(1, int(gap / factor))
        intercambiado = False
        for i in range(n - gap):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                intercambiado = True
    return lista


# === Comparison ===
def comparar_metodos_ordenamiento(lista, incluir_lentos=True, mostrar_resultados=True):
    """Compares execution times of all methods. Does not modify the original list."""
    metodos_rapidos = {
        "Merge Sort":       merge_sort,
        "Quick Sort":       quick_sort,
        "Heap Sort":        heap_sort,
        "Shell Sort":       shell_sort,
        "Tim Sort":         tim_sort,
        "Counting Sort":    counting_sort,
        "Radix Sort":       radix_sort,
        "Bucket Sort":      bucket_sort,
        "Python sorted()":  sorted,
    }

    metodos_lentos = {
        "Bubble Sort":         bubble_sort,
        "Bubble Sort Optim.":  bubble_sort_optimizado,
        "Selection Sort":      selection_sort,
        "Insertion Sort":      insertion_sort,
        "Cocktail Sort":       cocktail_sort,
        "Comb Sort":           comb_sort,
    }

    metodos = {}
    metodos.update(metodos_rapidos)
    if incluir_lentos:
        metodos.update(metodos_lentos)

    tiempos = {}
    n = len(lista)
    print(f"\nComparando métodos para lista de {n} elementos:")
    print("=" * 70)

    for nombre, metodo in metodos.items():
        lista_copia = lista.copy()
        inicio = time.time()
        try:
            resultado = metodo(lista_copia)
            tiempo = time.time() - inicio
            ordenada = esta_ordenada(resultado) if len(resultado) > 1 else True
            tiempos[nombre] = tiempo
            estado = "OK" if ordenada else "FAIL"
            print(f"{estado} {nombre:25s} {tiempo*1000:10.4f} ms")
        except Exception as e:
            print(f"ERR {nombre:25s} Error: {e}")
            tiempos[nombre] = float("inf")

    print("=" * 70)
    tiempos_validos = {k: v for k, v in tiempos.items() if v != float("inf")}
    if tiempos_validos:
        mas_rapido = min(tiempos_validos, key=tiempos_validos.get)
        print(f"\nMétodo más rápido: {mas_rapido} ({tiempos_validos[mas_rapido]*1000:.4f} ms)")
    return tiempos


if __name__ == "__main__":
    print("=== Comparación de TODOS los métodos de ordenamiento ===\n")

    print("--- Lista pequeña (20 elementos) ---")
    lista_peq = generar_lista_aleatoria(20, 1, 50)
    print(f"Lista: {lista_peq}")
    comparar_metodos_ordenamiento(lista_peq)

    print("\n--- Lista mediana (500 elementos) ---")
    lista_med = generar_lista_aleatoria(500, 1, 1000)
    comparar_metodos_ordenamiento(lista_med)

    print("\n--- Lista grande (5000 elementos, solo algoritmos rápidos) ---")
    lista_grande = generar_lista_aleatoria(5000, 1, 10000)
    comparar_metodos_ordenamiento(lista_grande, incluir_lentos=False)

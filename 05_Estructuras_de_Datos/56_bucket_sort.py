# -------------------------------------------------
# File Name: 56_bucket_sort.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Bucket Sort.
#              Distributes elements into buckets according to their value,
#              sorts each bucket with Insertion Sort and concatenates.
#              Ideal for uniformly distributed data. Includes versions
#              for floats [0,1), integers and negative numbers.
#              Step-by-step visualization.
#              Complexity: O(n + k) average, O(n²) worst case.
# -------------------------------------------------

import random
import time
import math


# ============================================================
# 1. Bucket Sort for floats [0, 1)
# ============================================================
def bucket_sort_float(lista):
    """
    Bucket Sort for floating point numbers in range [0, 1).
    Uses Insertion Sort within each bucket.
    Does not modify the original list.
    """
    if len(lista) <= 1:
        return lista.copy()

    lista = lista.copy()
    n = len(lista)
    buckets = [[] for _ in range(n)]

    # Distribute elements into buckets
    for num in lista:
        idx = int(n * num)  # Map [0, 1) to bucket index
        if idx == n:        # If num == 1.0, put in last bucket
            idx = n - 1
        buckets[idx].append(num)

    # Sort each bucket with Insertion Sort
    for bucket in buckets:
        insertion_sort_inplace(bucket)

    # Concatenate all buckets
    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)

    return resultado


def insertion_sort_inplace(lista):
    """Insertion Sort in-place (for sorting buckets)."""
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave


# ============================================================
# 2. Bucket Sort for integers (general range)
# ============================================================
def bucket_sort_int(lista, num_buckets=None):
    """
    Bucket Sort for integers with arbitrary range.
    Distribution based on relative value within range.
    """
    if len(lista) <= 1:
        return lista.copy()

    lista = lista.copy()
    min_val = min(lista)
    max_val = max(lista)

    if min_val == max_val:
        return lista  # All equal

    n = len(lista)
    if num_buckets is None:
        num_buckets = max(1, int(math.sqrt(n)))

    rango = max_val - min_val + 1
    buckets = [[] for _ in range(num_buckets)]

    # Distribute into buckets
    for num in lista:
        idx = int((num - min_val) / rango * num_buckets)
        if idx == num_buckets:
            idx = num_buckets - 1
        buckets[idx].append(num)

    # Sort each bucket
    for bucket in buckets:
        insertion_sort_inplace(bucket)

    # Concatenate
    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)

    return resultado


# ============================================================
# 3. Bucket Sort with visualization
# ============================================================
def bucket_sort_visual(lista, num_buckets=5):
    """Bucket Sort with process visualization."""
    if len(lista) <= 1:
        return lista.copy()

    lista = lista.copy()
    min_val = min(lista)
    max_val = max(lista)
    rango = max_val - min_val + 1

    buckets = [[] for _ in range(num_buckets)]

    print(f"\nLista original: {lista}")
    print(f"Rango: [{min_val}, {max_val}], Cubetas: {num_buckets}")
    print(f"{'='*60}")

    # Distribute
    for num in lista:
        idx = int((num - min_val) / rango * num_buckets)
        if idx == num_buckets:
            idx = num_buckets - 1
        buckets[idx].append(num)

    print("\nDespués de distribuir:")
    for i, bucket in enumerate(buckets):
        rango_cubeta = (min_val + i * rango // num_buckets,
                        min_val + (i + 1) * rango // num_buckets - 1)
        print(f"  Cubeta {i} [{rango_cubeta[0]:3d}-{rango_cubeta[1]:3d}]: {bucket}")

    # Sort each bucket
    for bucket in buckets:
        insertion_sort_inplace(bucket)

    print("\nDespués de ordenar cada cubeta:")
    for i, bucket in enumerate(buckets):
        print(f"  Cubeta {i}: {bucket}")

    # Concatenate
    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)

    print(f"\n{'='*60}")
    print(f"Resultado: {resultado}")
    return resultado


# ============================================================
# 4. Bucket Sort for negatives
# ============================================================
def bucket_sort_negatives(lista):
    """
    Bucket Sort that handles negative numbers.
    Separates negatives and positives, sorts separately, merges.
    """
    if len(lista) <= 1:
        return lista.copy()

    negativos = [-x for x in lista if x < 0]
    positivos = [x for x in lista if x >= 0]

    neg_sorted = bucket_sort_int(negativos) if negativos else []
    pos_sorted = bucket_sort_int(positivos) if positivos else []

    # Reverse negatives and negate back
    return [-x for x in reversed(neg_sorted)] + pos_sorted


# ============================================================
# 5. Comparison with other algorithms
# ============================================================
def comparar(n=5000):
    """Compares Bucket Sort with other methods."""
    # Uniformly distributed data (ideal case for Bucket Sort)
    lista_float = [random.random() for _ in range(n)]
    lista_int = [random.randint(1, 10000) for _ in range(n)]

    print(f"\n--- Comparación con {n} flotantes uniformes [0, 1) ---")
    print("=" * 50)

    inicio = time.time()
    bucket_sort_float(lista_float)
    t_bucket = time.time() - inicio
    print(f"  Bucket Sort:     {t_bucket*1000:8.2f} ms")

    inicio = time.time()
    sorted(lista_float)
    t_sorted = time.time() - inicio
    print(f"  Python sorted(): {t_sorted*1000:8.2f} ms")

    print(f"\n--- Comparación con {n} enteros [1, 10000] ---")
    print("=" * 50)

    inicio = time.time()
    bucket_sort_int(lista_int)
    t_bucket_i = time.time() - inicio
    print(f"  Bucket Sort:     {t_bucket_i*1000:8.2f} ms")

    inicio = time.time()
    sorted(lista_int)
    t_sorted_i = time.time() - inicio
    print(f"  Python sorted(): {t_sorted_i*1000:8.2f} ms")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Bucket Sort ===\n")

    # Visual demo
    lista_demo = [29, 25, 3, 49, 9, 37, 21, 43, 15, 33]
    bucket_sort_visual(lista_demo, num_buckets=5)

    # Float tests
    print("\n--- Prueba flotantes [0, 1) ---")
    floats = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    resultado = bucket_sort_float(floats)
    print(f"  Original:  {floats}")
    print(f"  Ordenada:  {resultado}")

    # Tests with negatives
    print("\n--- Prueba con negativos ---")
    negativos = [5, -3, 8, -1, 0, -7, 3, -2, 6, -5]
    resultado_neg = bucket_sort_negatives(negativos)
    print(f"  Original:  {negativos}")
    print(f"  Ordenada:  {resultado_neg}")

    # Edge cases
    print("\n--- Casos especiales ---")
    casos = {
        "Ya ordenada":  list(range(1, 11)),
        "Inversa":      list(range(10, 0, -1)),
        "Iguales":      [5] * 8,
        "Un elemento":  [42],
        "Vacía":        [],
    }
    for nombre, caso in casos.items():
        res = bucket_sort_int(caso) if caso else []
        ok = all(res[i] <= res[i + 1] for i in range(len(res) - 1)) if len(res) > 1 else True
        print(f"  {nombre:15s}: {caso} -> {res} {'OK' if ok else 'FAIL'}")

    # Performance comparison
    comparar(3000)

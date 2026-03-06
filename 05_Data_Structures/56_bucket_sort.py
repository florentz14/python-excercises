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

    # Distribute: each float in [0,1) maps to bucket idx = int(n * num)
    for num in lista:
        idx = int(n * num)  # Map [0, 1) to bucket index 0..n-1
        if idx == n:        # Edge case: num == 1.0 -> last bucket
            idx = n - 1
        buckets[idx].append(num)

    # Sort each bucket (Insertion Sort is stable and good for small lists)
    for bucket in buckets:
        insertion_sort_inplace(bucket)

    # Concatenate buckets in order to get sorted result
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


def insertion_sort_inplace(arr):
    """
    Insertion Sort in-place. Used for sorting individual buckets.
    Efficient for small lists (typical bucket size).
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift larger elements right
            j -= 1
        arr[j + 1] = key  # Insert at correct position


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
        return lista  # All elements equal

    n = len(lista)
    if num_buckets is None:
        num_buckets = max(1, int(math.sqrt(n)))  # sqrt(n) buckets is common choice

    range_val = max_val - min_val + 1
    buckets = [[] for _ in range(num_buckets)]

    # Distribute: map value to bucket based on position in [min_val, max_val]
    for num in lista:
        idx = int((num - min_val) / range_val * num_buckets)
        if idx == num_buckets:
            idx = num_buckets - 1
        buckets[idx].append(num)

    # Sort each bucket, concatenate
    result = []
    for bucket in buckets:
        insertion_sort_inplace(bucket)
        result.extend(bucket)

    return result


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
    range_val = max_val - min_val + 1

    buckets = [[] for _ in range(num_buckets)]

    print(f"\nOriginal: {lista}")
    print(f"Range: [{min_val}, {max_val}], Buckets: {num_buckets}")
    print("=" * 60)

    # Distribute elements into buckets
    for num in lista:
        idx = int((num - min_val) / range_val * num_buckets)
        if idx == num_buckets:
            idx = num_buckets - 1
        buckets[idx].append(num)

    print("\nAfter distribution:")
    for i, bucket in enumerate(buckets):
        bucket_range = (min_val + i * range_val // num_buckets,
                        min_val + (i + 1) * range_val // num_buckets - 1)
        print(f"  Bucket {i} [{bucket_range[0]:3d}-{bucket_range[1]:3d}]: {bucket}")

    # Sort each bucket with Insertion Sort
    for bucket in buckets:
        insertion_sort_inplace(bucket)

    print("\nAfter sorting each bucket:")
    for i, bucket in enumerate(buckets):
        print(f"  Bucket {i}: {bucket}")

    # Concatenate buckets to get final sorted list
    result = []
    for bucket in buckets:
        result.extend(bucket)

    print(f"\n{'='*60}")
    print(f"Result: {result}")
    return result


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

    # Split into negatives and non-negatives
    negatives = [-x for x in lista if x < 0]
    positives = [x for x in lista if x >= 0]

    neg_sorted = bucket_sort_int(negatives) if negatives else []
    pos_sorted = bucket_sort_int(positives) if positives else []

    # Negatives: sort as positive, then reverse and negate for ascending order
    return [-x for x in reversed(neg_sorted)] + pos_sorted


# ============================================================
# 5. Comparison with other algorithms
# ============================================================
def compare_performance(n=5000):
    """Compares Bucket Sort with Python sorted() on different data types."""
    floats = [random.random() for _ in range(n)]
    ints = [random.randint(1, 10000) for _ in range(n)]

    print(f"\n--- Comparison with {n} uniform floats [0, 1) ---")
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
    print("\n--- Test floats [0, 1) ---")
    floats = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    resultado = bucket_sort_float(floats)
    print(f"  Original:  {floats}")
    print(f"  Sorted:    {resultado}")

    # Tests with negatives
    print("\n--- Test with negatives ---")
    negativos = [5, -3, 8, -1, 0, -7, 3, -2, 6, -5]
    resultado_neg = bucket_sort_negatives(negativos)
    print(f"  Original:  {negativos}")
    print(f"  Sorted:    {resultado_neg}")

    # Edge cases
    print("\n--- Edge cases ---")
    cases = {
        "Sorted":   list(range(1, 11)),
        "Reverse":  list(range(10, 0, -1)),
        "All same": [5] * 8,
        "Single":   [42],
        "Empty":    [],
    }
    for name, case in cases.items():
        res = bucket_sort_int(case) if case else []
        ok = all(res[i] <= res[i + 1] for i in range(len(res) - 1)) if len(res) > 1 else True
        print(f"  {name:15s}: {case} -> {res} {'OK' if ok else 'FAIL'}")

    # Performance comparison
    compare_performance(3000)

# -------------------------------------------------
# File Name: 51_comparison.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Sorting algorithm comparison. Performance benchmarks.
# -------------------------------------------------

import time
import random
import math


# === Utilities ===
def is_sorted(items):
    """Checks if a list is sorted in ascending order."""
    return all(items[i] <= items[i + 1] for i in range(len(items) - 1))


def generate_random_list(n, minimum=1, maximum=100):
    """Generates a random list of n elements."""
    return [random.randint(minimum, maximum) for _ in range(n)]


# === Bubble Sort ===
def bubble_sort(items):
    """Classic bubble sort. Does not modify the original list."""
    items = items.copy()
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def bubble_sort_optimized(items):
    """Stops if no swaps occur (list already sorted)."""
    items = items.copy()
    n = len(items)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


# === Selection Sort ===
def selection_sort(items):
    """At each step places the minimum of the rest at the current position."""
    items = items.copy()
    n = len(items)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
    return items


# === Insertion Sort ===
def insertion_sort(items):
    """Inserts each element into its place within the already sorted portion."""
    items = items.copy()
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
    return items


# === Merge Sort ===
def merge(left, right):
    """Merges two sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(items):
    """Divide and conquer: divide, sort halves, merge."""
    if len(items) <= 1:
        return items.copy()
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)


# === Quick Sort ===
def quick_sort(items):
    """Version that uses auxiliary lists (clear). Pivot: middle element."""
    if len(items) <= 1:
        return items.copy()
    pivot = items[len(items) // 2]
    lower = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    greater = [x for x in items if x > pivot]
    return quick_sort(lower) + equal + quick_sort(greater)


# === Heap Sort ===
def heapify(items, n, i):
    """Adjusts the tree so that the root at i is a max-heap."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and items[left] > items[largest]:
        largest = left
    if right < n and items[right] > items[largest]:
        largest = right
    if largest != i:
        items[i], items[largest] = items[largest], items[i]
        heapify(items, n, largest)


def heap_sort(items):
    """Builds max heap and repeatedly extracts the maximum."""
    items = items.copy()
    n = len(items)
    for i in range(n // 2 - 1, -1, -1):
        heapify(items, n, i)
    for i in range(n - 1, 0, -1):
        items[0], items[i] = items[i], items[0]
        heapify(items, i, 0)
    return items


# === Counting Sort ===
def counting_sort(items, maximum=None):
    """Sorts by counting occurrences of each value (non-negative integers)."""
    if not items:
        return []
    if maximum is None:
        maximum = max(items) if items else 0
    count = [0] * (maximum + 1)
    for num in items:
        count[num] += 1
    result = []
    for i in range(maximum + 1):
        result.extend([i] * count[i])
    return result


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


def radix_sort(items):
    """Radix Sort (LSD): sorts digit by digit from least significant."""
    if not items:
        return []
    items = items.copy()
    max_val = max(items)
    exp = 1
    while max_val // exp > 0:
        items = counting_sort_by_digit(items, exp)
        exp *= 10
    return items


# === Shell Sort ===
def shell_sort(items):
    """Shell Sort with Knuth gap sequence."""
    items = items.copy()
    n = len(items)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, n):
            temp = items[i]
            j = i
            while j >= gap and items[j - gap] > temp:
                items[j] = items[j - gap]
                j -= gap
            items[j] = temp
        gap //= 3
    return items


# === Bucket Sort ===
def bucket_sort(items):
    """Bucket Sort for integers with arbitrary range."""
    if len(items) <= 1:
        return items.copy()
    items = items.copy()
    min_value = min(items)
    max_value = max(items)
    if min_value == max_value:
        return items
    n = len(items)
    num_buckets = max(1, int(math.sqrt(n)))
    value_range = max_value - min_value + 1
    buckets = [[] for _ in range(num_buckets)]
    for num in items:
        idx = int((num - min_value) / value_range * num_buckets)
        if idx == num_buckets:
            idx = num_buckets - 1
        buckets[idx].append(num)
    for bucket in buckets:
        bucket.sort()
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result


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
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


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


def tim_sort(items):
    """Tim Sort: hybrid of Merge Sort + Insertion Sort."""
    arr = items.copy()
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
def cocktail_sort(items):
    """Cocktail Sort: bidirectional Bubble Sort."""
    items = items.copy()
    n = len(items)
    start = 0
    end = n - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        end -= 1
        if not swapped:
            break
        swapped = False
        for i in range(end, start, -1):
            if items[i] < items[i - 1]:
                items[i], items[i - 1] = items[i - 1], items[i]
                swapped = True
        start += 1
    return items


# === Comb Sort ===
def comb_sort(items):
    """Comb Sort: Bubble Sort with decreasing gaps (factor 1.3)."""
    items = items.copy()
    n = len(items)
    gap = n
    factor = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = max(1, int(gap / factor))
        swapped = False
        for i in range(n - gap):
            if items[i] > items[i + gap]:
                items[i], items[i + gap] = items[i + gap], items[i]
                swapped = True
    return items


# === Comparison ===
def compare_sorting_methods(items, include_slow=True, show_results=True):
    """Compares execution times of all methods. Does not modify the original list."""
    fast_methods = {
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

    slow_methods = {
        "Bubble Sort":         bubble_sort,
        "Bubble Sort Optim.":  bubble_sort_optimized,
        "Selection Sort":      selection_sort,
        "Insertion Sort":      insertion_sort,
        "Cocktail Sort":       cocktail_sort,
        "Comb Sort":           comb_sort,
    }

    methods = {}
    methods.update(fast_methods)
    if include_slow:
        methods.update(slow_methods)

    times = {}
    n = len(items)
    print(f"\nComparing methods for list of {n} elements:")
    print("=" * 70)

    for name, method in methods.items():
        list_copy = items.copy()
        start = time.time()
        try:
            result = method(list_copy)
            elapsed = time.time() - start
            sorted_ok = is_sorted(result) if len(result) > 1 else True
            times[name] = elapsed
            status = "OK" if sorted_ok else "FAIL"
            print(f"{status} {name:25s} {elapsed*1000:10.4f} ms")
        except Exception as e:
            print(f"ERR {name:25s} Error: {e}")
            times[name] = float("inf")

    print("=" * 70)
    valid_times = {k: v for k, v in times.items() if v != float("inf")}
    if valid_times:
        fastest = min(valid_times, key=valid_times.get)
        print(f"\nFastest method: {fastest} ({valid_times[fastest]*1000:.4f} ms)")
    return times


if __name__ == "__main__":
    print("=== Comparison of ALL sorting methods ===\n")

    print("--- Small list (20 elements) ---")
    small_list = generate_random_list(20, 1, 50)
    print(f"List: {small_list}")
    compare_sorting_methods(small_list)

    print("\n--- Medium list (500 elements) ---")
    medium_list = generate_random_list(500, 1, 1000)
    compare_sorting_methods(medium_list)

    print("\n--- Large list (5000 elements, fast algorithms only) ---")
    large_list = generate_random_list(5000, 1, 10000)
    compare_sorting_methods(large_list, include_slow=False)


# Backward-compatible aliases.
esta_ordenada = is_sorted
generar_lista_aleatoria = generate_random_list
bubble_sort_optimizado = bubble_sort_optimized
comparar_metodos_ordenamiento = compare_sorting_methods

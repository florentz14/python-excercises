# 05_Data_Structures

Sorting, search, greedy, string, mathematical, backtracking algorithms and advanced structures.

## Greedy Algorithms (01-06)

| File | Content |
|------|---------|
| `01_fractional_knapsack.py` | Fractional knapsack (value/weight, O(n log n)) |
| `02_activity_selection.py` | Activity selection (sort by finish, O(n log n)) |
| `03_kruskal.py` | MST with Kruskal (Union-Find, O(E log E)) |
| `04_huffman.py` | Huffman coding (heap, O(n log n)) |
| `05_coin_change.py` | Greedy coin change (canonical systems only) |
| `06_interval_scheduling.py` | Weighted interval scheduling (simplified) |

## String Algorithms (08-14)

| File | Content |
|------|---------|
| `08_rabin_karp.py` | Rabin-Karp (rolling hash search, O(n+m) avg) |
| `09_z_algorithm.py` | Z-Algorithm (Z-array and pattern search, O(n+m)) |
| `10_longest_common_substring.py` | Longest common substring (DP, O(m*n)) |
| `11_edit_distance.py` | Levenshtein distance (insert/delete/substitute, O(m*n)) |
| `12_longest_palindromic_substring.py` | Longest palindromic substring (center expansion, O(n²)) |
| `13_anagrams.py` | Anagrams: check and group |
| `14_string_permutations.py` | String permutations (recursive, O(n!)) |

## Mathematical Algorithms (15-21)

| File | Content |
|------|---------|
| `15_pascal.py` | Pascal's triangle, binomial coefficients, row n |
| `16_euclid.py` | GCD (iterative/recursive), LCM, extended Euclid |
| `17_eratosthenes.py` | Sieve of Eratosthenes, `is_prime()` |
| `18_modular_exponentiation.py` | Fast modular exponentiation (base^exp mod m) |
| `19_fibonacci_mathematical.py` | Fibonacci: Binet and matrix exponentiation |
| `20_prime_factorization.py` | Prime factorization, unique factors, divisor count |
| `21_base_conversion.py` | Base conversion (decimal, binary, octal, hex) |

## Backtracking (23-28)

| File | Content |
|------|---------|
| `23_n_queens.py` | N-Queens: place N queens without attacking |
| `24_sudoku.py` | Sudoku 9x9 solver |
| `25_maze.py` | Maze solving (path from start to goal) |
| `26_permutations_backtracking.py` | Permutation generation |
| `27_combinations_backtracking.py` | Combinations of k from n |
| `28_subset_sum.py` | Subset Sum (subsets summing to target) |
| `60_word_search.py` | Word Search (backtracking on grid, LeetCode 79) |

## Heap / Priority Queue (49, 61-63)

| File | Content |
|------|---------|
| `49_heap.py` | Heap Sort and heapify |
| `61_k_closest_points_to_origin.py` | K Closest Points (heapq, LeetCode 973) |
| `62_kth_largest_element.py` | Kth Largest Element (heap, LeetCode 215) |
| `63_priority_queue_heapq.py` | Priority Queue with heapq |

## Two Pointers (64)

| File | Content |
|------|---------|
| `64_two_pointers_pattern.py` | Palindrome, Two Sum sorted, Max Area |

## Advanced Data Structures (30-33)

| File | Content |
|------|---------|
| `30_trie.py` | Trie (prefix tree): insert, search, autocomplete |
| `31_segment_tree.py` | Segment Tree: range query/update (sum, min, max) |
| `32_fenwick_tree.py` | Fenwick Tree (BIT): prefix and range sums |
| `33_union_find_improved.py` | Union-Find with path compression and union by rank |

## Search Algorithms (35-40)

| File | Content |
|------|---------|
| `35_linear_search.py` | Linear search, optimized, all occurrences |
| `36_binary_search.py` | Binary search (iterative, recursive, first/last) |
| `36a_binary_search_fundamentals.py` | Classic vs optimized (safe mid), O(log n) |
| `36b_binary_search_interview_variants.py` | 7 variants: Normal, First/Last, Insert, Peak, Rotated, Find First True |
| `36c_binary_search_workshop.py` | Mini workshop: 10 exercises (easy → interview) |
| `37_strings.py` | Pattern search in text (brute force) |
| `38_kmp.py` | KMP algorithm (Knuth-Morris-Pratt) |
| `39_comparison.py` | Compare linear vs binary and brute vs KMP |
| `40_utilities.py` | Insert position, occurrence count in sorted list |

**Note:** 39 and 40 are self-contained.

## Other (42)

| File | Content |
|------|---------|
| `42_dataclass_inventory.py` | Dataclass example for inventory |

## Sorting Methods (43-54)

| File | Content |
|------|---------|
| `43_sort_utilities.py` | `is_sorted()`, `generate_random_list()` |
| `44_bubble.py` | Bubble Sort and optimized version |
| `45_selection.py` | Selection Sort |
| `46_insertion.py` | Insertion Sort |
| `47_merge.py` | Merge Sort and `merge()` |
| `48_quick.py` | Quick Sort and Quick Sort in-place |
| `49_heap.py` | Heap Sort and `heapify()` |
| `50_counting.py` | Counting Sort (small range) |
| `51_comparison.py` | Compare timing of all methods |
| `52_complexity.py` | Complexity table (best/avg/worst) |
| `53_special_cases.py` | Cases: sorted, reverse, equals, empty |
| `54_radix_sort.py` | Radix Sort (digit-by-digit) |

**Note:** 51 and 53 include all necessary functions (self-contained).

## Sorting Summary

| Method | Complexity | Notes |
|--------|------------|-------|
| Bubble Sort | O(n²) | Simple, stable |
| Selection Sort | O(n²) | Simple, not stable |
| Insertion Sort | O(n²) worst, O(n) best | Stable, good for nearly sorted lists |
| Merge Sort | O(n log n) | Stable, extra memory |
| Quick Sort | O(n log n) average | In-place, not stable |
| Heap Sort | O(n log n) | In-place, not stable |
| Counting Sort | O(n + k) | Known small range |
| Radix Sort | O(d * (n + k)) | d = digits, stable, non-comparative |
| Python `sorted()` | O(n log n) | Timsort (hybrid) |

### Usage recommendations

1. **Small lists (< 50):** Insertion Sort or Bubble Sort
2. **Medium lists (50-1000):** Quick Sort or Merge Sort
3. **Large lists (> 1000):** Quick Sort, Merge Sort, Heap Sort or `sorted()`
4. **Known small value range:** Counting Sort
5. **Integers with few digits:** Radix Sort (better than O(n log n) when d < log n)
6. **Need stability:** Merge, Insertion, Bubble, Counting, Radix (avoid Quick, Heap)
7. **Limited space (in-place):** Quick Sort, Heap Sort, Insertion Sort (avoid Merge)

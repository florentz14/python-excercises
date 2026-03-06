# Audit: 20 Fundamental Algorithms

Comparison between the project and the 20 fundamental algorithms guide.

| # | Algorithm | Status | Location | Notes |
|---|-----------|--------|----------|-------|
| 1 | **Linear Search** | ✅ Present | `05_Data_Structures/35_linear_search.py` | `busqueda_lineal`, optimized, all occurrences |
| 2 | **Binary Search** | ✅ Present | `05_Data_Structures/36_binary_search.py`, 36a, 36b, 36c, 36d | Multiple variants |
| 3 | **Bubble Sort** | ✅ Present | `05_Data_Structures/44_bubble.py` | Classic + optimized |
| 4 | **Selection Sort** | ✅ Present | `05_Data_Structures/45_selection.py` | |
| 5 | **Insertion Sort** | ✅ Present | `05_Data_Structures/46_insertion.py` | |
| 6 | **Merge Sort** | ✅ Present | `05_Data_Structures/47_merge.py` | merge_sort + _merge |
| 7 | **Quick Sort** | ✅ Present | `05_Data_Structures/48_quick.py` | Classic + in-place |
| 8 | **BFS** | ✅ Present | `15_Graphs/03_bfs.py`, `13_Queues/07_bfs_graph.py` | Uses deque |
| 9 | **DFS** | ✅ Present | `15_Graphs/04_dfs.py` | Recursive; 05_lista_adyacencia has iterative |
| 10 | **Dijkstra** | ⚠️ Present (naive) | `15_Graphs/08_dijkstra.py` | O(V²) without heap; guide uses heapq O((V+E)log V) |
| 11 | **Kadane** | ✅ Present | `05_Data_Structures/65_kadane_max_subarray.py` | max_subarray_sum |
| 12 | **Two Pointers** | ✅ Present | `05_Data_Structures/64_two_pointers_pattern.py` | Palindrome, Two Sum, Max Area |
| 13 | **Sliding Window** | ✅ Present | `01_Variables_and_Types/operations/09_max_subarray_sum_sliding_window.py` | Max sum of subarray of size k |
| 14 | **Prefix Sum** | ✅ Present | `05_Data_Structures/66_prefix_sum.py` | build_prefix_sum, range_sum |
| 15 | **Hash Map Counting** | ✅ Present | `05_Data_Structures/67_frequency_count.py` | frequency_count |
| 16 | **Union-Find** | ✅ Present | `05_Data_Structures/33_union_find_improved.py` | Path compression + union by rank |
| 17 | **Top K with Heap** | ✅ Present | `05_Data_Structures/61_k_closest_points_to_origin.py`, `62_kth_largest_element.py` | |
| 18 | **Backtracking (Subsets)** | ✅ Present | `05_Data_Structures/68_backtracking_subsets.py` | subsets (choose/explore/unchoose) |
| 19 | **DP Fibonacci** | ✅ Present | `05_Data_Structures/19_fibonacci_mathematical.py` | fibonacci_dp (iterative O(n) O(1)) |
| 20 | **KMP** | ✅ Present | `05_Data_Structures/38_kmp.py` | LPS table, first/all occurrences |

---

## Optional Improvement

### Dijkstra with Heap ⚠️
- **Purpose:** O((V+E) log V) with `heapq` (guide's version).
- **Current:** `15_Graphs/08_dijkstra.py` uses O(V²) linear scan.
- **Change:** Add heap-based variant if needed for large graphs.

---

## Summary

| Status | Count |
|--------|-------|
| ✅ Complete | 19 |
| ⚠️ Partial (Dijkstra naive) | 1 |

**All 20 algorithms from the guide are now present.** Dijkstra exists but uses O(V²) instead of heap-based O((V+E) log V); optional upgrade if needed.

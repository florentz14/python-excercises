# 18_Linked_Lists

Comprehensive linked list algorithms and data structures. From basic implementations to advanced interview problems.

## Files

| File | Content |
| --- | --- |
| `01_singly_linked_list.py` | Singly linked list (single `next` pointer) |
| `02_doubly_linked_list.py` | Doubly linked list (`prev` and `next`) |
| `03_circular_linked_list.py` | Circular linked list (last points to first) |
| `04_linked_list_operations.py` | Common operations (`reverse`, `merge`, `find middle`, cycle) |
| `05_insert_operations.py` | Insertion operations (beginning, end, position, after node) |
| `06_delete_operations.py` | Deletion operations (head, tail, by value, by position) |
| `07_reverse_linked_list.py` | Reverse linked list (iterative and recursive) |
| `08_find_middle.py` | Find middle node (slow/fast pointers) |
| `09_cycle_detection_floyd.py` | Detect cycles (Floyd's Tortoise and Hare) |
| `10_merge_two_sorted_lists.py` | Merge two sorted linked lists |
| `11_remove_duplicates.py` | Remove duplicates (sorted and unsorted) |
| `12_intersection_of_lists.py` | Find intersection of two linked lists |
| `13_kth_from_end.py` | Find k-th node from the end |
| `14_partition_list.py` | Partition list around a pivot value |
| `15_lru_cache_simulation.py` | LRU cache simulation (list + hashmap) |
| `16_singly_linked_list_full_operations.py` | Full singly linked list walkthrough with extended operations |
| `17_doubly_linked_list_full_operations.py` | Full doubly linked list walkthrough with bidirectional ops |
| `18_circular_linked_list_full_operations.py` | Full circular linked list walkthrough (singly + doubly) |
| `19_skip_list_full_operations.py` | Skip list with probabilistic levels and full operation demos |
| `20_palindrome_linked_list.py` | Check if linked list is a palindrome |
| `21_reorder_list.py` | Reorder list as L0 -> Ln -> L1 -> Ln-1 |
| `22_swap_nodes_in_pairs.py` | Swap each pair of adjacent nodes |
| `23_reverse_nodes_in_k_group.py` | Reverse nodes in groups of size k |
| `24_add_two_numbers_linked_list.py` | Add two numbers represented as linked lists |
| `25_copy_list_with_random_pointer.py` | Deep copy list with next and random pointers |
| `26_rotate_list.py` | Rotate linked list to the right by k steps |
| `27_remove_nth_node_from_end.py` | Remove the n-th node from the end |
| `28_flatten_multilevel_doubly_linked_list.py` | Flatten multilevel doubly linked list |
| `29_sort_list_merge_sort.py` | Sort linked list with merge sort |
| `30_linked_list_cycle_ii.py` | Find where a cycle starts |
| `31_reverse_linked_list_ii.py` | Reverse a sublist from left to right |
| `32_odd_even_linked_list.py` | Group odd-indexed nodes then even-indexed nodes |
| `33_merge_k_sorted_lists.py` | Merge k sorted linked lists |
| `34_remove_zero_sum_consecutive_nodes.py` | Remove zero-sum consecutive node sequences |
| `35_split_linked_list_in_parts.py` | Split list into k consecutive parts |
| `36_reverse_nodes_in_even_length_groups.py` | Reverse nodes in even-length natural groups |
| `37_nodes_between_critical_points.py` | Find min/max distance between critical points |
| `38_delete_the_middle_node.py` | Delete the middle node of a linked list |
| `39_maximum_twin_sum_of_linked_list.py` | Maximum twin sum in even-length list |
| `40_insert_greatest_common_divisors.py` | Insert GCD nodes between adjacent nodes |
| `41_remove_duplicates_from_sorted_list_ii.py` | Remove all duplicates from sorted list |
| `42_swap_nodes_in_linked_list.py` | Swap k-th node from start and end |
| `43_next_greater_node_in_linked_list.py` | Next greater value for each node |
| `44_linked_list_components.py` | Count connected components in a subset |
| `45_convert_binary_number_in_linked_list_to_integer.py` | Convert binary linked list to integer |
| `46_merge_in_between_linked_lists.py` | Replace a range with another linked list |
| `47_double_a_number_represented_as_linked_list.py` | Double number stored in linked list |
| `48_remove_nodes_from_linked_list.py` | Remove nodes with greater value on right |
| `49_delete_nodes_from_linked_list_present_in_array.py` | Delete nodes whose values appear in array |
| `50_insert_into_a_sorted_circular_linked_list.py` | Insert value in sorted circular list |

## Concepts

### Singly Linked List

```
[data|next] -> [data|next] -> [data|next] -> None
```

### Doubly Linked List

```
None <- [prev|data|next] <-> [prev|data|next] <-> [prev|data|next] -> None
```

### Circular Linked List

```
[data|next] -> [data|next] -> [data|next] --+
     ^                                       |
     +---------------------------------------+
```

## Implemented Algorithms

| Algorithm | Complexity | Use Case |
| --- | --- | --- |
| Reverse List | O(n) | Reverse node order |
| Find Middle | O(n) | Slow/Fast pointers |
| Cycle Detection | O(n) | Floyd's Tortoise and Hare |
| Merge Sorted Lists | O(m+n) | Merge sorted linked lists |
| Remove Duplicates | O(n) | Hash set for unsorted list |
| Find Intersection | O(m+n) | Y-shaped list intersection |
| Kth from End | O(n) | Two pointers |
| Partition | O(n) | Reorder around pivot |
| LRU Cache | O(1) | List + hashmap cache |
| Palindrome Check | O(n) | Compare list with reverse |
| Reorder List | O(n) | Split, reverse, merge |
| Swap in Pairs | O(n) | Local pointer rewiring |
| Reverse in k Group | O(n) | Group-based in-place reverse |
| Add Two Numbers | O(max(m,n)) | Digit-by-digit linked sum |
| Random List Copy | O(n) | Deep copy with hash map |
| Rotate List | O(n) | Circular shift of nodes |
| Remove Nth from End | O(n) | Two-pointer gap method |
| Flatten Multilevel | O(n) | Stack-based DFS flatten |
| Sort List | O(n log n) | Merge sort on linked list |
| Cycle Entry Point | O(n) | Floyd + meeting-point proof |
| Reverse Sublist | O(n) | In-place segment reversal |
| Odd-Even Grouping | O(n) | Pointer regrouping by index |
| Merge K Lists | O(n log k) | Heap-based list merging |
| Remove Zero Sums | O(n) | Prefix-sum node skipping |
| Split in Parts | O(n) | Balanced partitioning |
| Reverse Even Groups | O(n) | Grouped conditional reverse |
| Critical Points | O(n) | Local extrema distance |
| Delete Middle Node | O(n) | Slow/fast middle removal |
| Maximum Twin Sum | O(n) | Half-reverse + pair scan |
| Insert GCD Nodes | O(n) | Arithmetic node insertion |
| Remove Duplicates II | O(n) | Skip repeated sorted blocks |
| Swap Kth Nodes | O(n) | Two-pointer symmetric swap |
| Next Greater Nodes | O(n) | Monotonic stack on values |
| List Components | O(n) | Set-based component counting |
| Binary to Integer | O(n) | Bitwise accumulation |
| Merge In Between | O(n+m) | Range splice with tail join |
| Double Number | O(n) | Reverse, process carry, undo |
| Remove Nodes Right | O(n) | Reverse and running maximum |
| Delete by Array | O(n+m) | Hash set filtering |
| Circular Insert | O(n) | Ordered insertion in cycle |

## Operations

| Operation | Time |
| --- | --- |
| Index access | O(n) |
| Insert at head | O(1) |
| Insert at tail | O(n) / O(1)\* |
| Search | O(n) |
| Delete | O(n) |

\*O(1) if we keep a tail reference

## Run

```bash
python 16_singly_linked_list_full_operations.py
python 19_skip_list_full_operations.py
python 20_palindrome_linked_list.py
python 23_reverse_nodes_in_k_group.py
python 25_copy_list_with_random_pointer.py
python 29_sort_list_merge_sort.py
python 30_linked_list_cycle_ii.py
python 33_merge_k_sorted_lists.py
python 35_split_linked_list_in_parts.py
python 37_nodes_between_critical_points.py
python 40_insert_greatest_common_divisors.py
python 43_next_greater_node_in_linked_list.py
python 45_convert_binary_number_in_linked_list_to_integer.py
python 47_double_a_number_represented_as_linked_list.py
python 50_insert_into_a_sorted_circular_linked_list.py
```

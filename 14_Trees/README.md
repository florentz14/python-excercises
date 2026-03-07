# 14_Trees

Tree data structures and algorithms. Covers binary trees, BST, AVL, Red-Black, B-Tree, Heap, Trie, Segment Tree, Fenwick Tree, KD-Tree, plus **25 classic interview problems**.

## Tree Types (01-18)

| File | Content |
|------|---------|
| `01_node.py` | Basic tree node |
| `02_traversal.py` | Basic traversals |
| `03_height.py` | Tree height |
| `04_basic_binary.py` | Binary tree |
| `05_traversals.py` | Preorder, inorder, postorder, level order |
| `06_bst.py` | Binary Search Tree |
| `07_avl.py` | AVL tree (self-balancing) |
| `08_nary.py` | N-ary tree |
| `09_operations.py` | Common operations |
| `10_summary.py` | Summary of tree types |
| `11_red_black.py` | Red-Black tree |
| `12_b_tree.py` | B-Tree |
| `13_heap.py` | Min/Max heap |
| `14_trie.py` | Trie (prefix tree) |
| `15_segment_tree.py` | Segment tree (range queries) |
| `16_fenwick_tree.py` | Fenwick tree (BIT) |
| `17_kd_tree.py` | KD-Tree (multidimensional) |
| `18_b_plus_tree.py` | B+ Tree (conceptual) |

**Helper modules:** `basic_binary.py`, `traversals.py`, `bst.py` (for imports from numbered files)

## 25 Classic Tree Problems

Professional list used in **Google, Amazon, Meta, Microsoft** interviews. See [`classic_problems/README.md`](classic_problems/README.md) for full details.

| # | Problem | # | Problem |
|---|---------|---|---------|
| 01 | Maximum Depth | 14 | Path Sum |
| 02 | Minimum Depth | 15 | Path Sum II |
| 03 | Invert Binary Tree | 16 | Maximum Path Sum |
| 04 | Same Tree | 17 | Binary Tree Paths |
| 05 | Symmetric Tree | 18 | LCA (Binary Tree) |
| 06 | Preorder Traversal | 19 | LCA (BST) |
| 07 | Inorder Traversal | 20 | Sorted Array to BST |
| 08 | Postorder Traversal | 21 | BST to Sorted List |
| 09 | Level Order Traversal | 22 | Serialize/Deserialize |
| 10 | Validate BST | 23 | Diameter of Tree |
| 11 | Search in BST | 24 | Balanced Tree |
| 12 | Insert into BST | 25 | Kth Smallest in BST |
| 13 | Delete in BST | | |

### Top 10 Essential

1. Maximum Depth  
2. Invert Binary Tree  
3. Validate BST  
4. Level Order Traversal  
5. Path Sum  
6. Lowest Common Ancestor  
7. Diameter of Binary Tree  
8. Balanced Binary Tree  
9. Kth Smallest Element in BST  
10. Serialize / Deserialize Tree  

## Run

```bash
# Tree types
python 04_basic_binary.py
python 06_bst.py
python 08_dijkstra.py

# Classic problems
cd classic_problems
python 01_max_depth.py
python 03_invert_tree.py
python 25_kth_smallest_bst.py
```

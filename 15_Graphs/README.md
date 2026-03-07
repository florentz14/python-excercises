# 15_Graphs

Graph data structures and algorithms. Professional core list for interviews (Google, Amazon, competitive programming, AI pathfinding, network routing).

## Professional Core List ✓

| Algorithm | File | Status |
|-----------|------|--------|
| BFS | `03_bfs.py` | ✓ |
| DFS | `04_dfs.py` | ✓ |
| Dijkstra | `08_dijkstra.py` | ✓ |
| Bellman-Ford | `14_bellman_ford.py` | ✓ |
| Floyd-Warshall | `15_floyd_warshall.py` | ✓ |
| A* | `16_a_star.py` | ✓ |
| Topological Sort | `10_topological_sort.py` | ✓ |
| Union-Find | `17_union_find.py` | ✓ |
| Kruskal (MST) | `18_kruskal.py` | ✓ |
| Prim (MST) | `19_prim.py` | ✓ |
| Tarjan SCC | `20_tarjan_scc.py` | ✓ |
| Ford-Fulkerson | `21_ford_fulkerson.py` | ✓ |

## Structure Overview

| Category | Files | Content |
|----------|-------|---------|
| **Representations** | 01, 02, 05, 06 | Adjacency list, class, matrix |
| **Traversal** | 03, 04, 23 | BFS, DFS, multi-source BFS |
| **Shortest Paths** | 08, 14, 15, 16 | Dijkstra, Bellman-Ford, Floyd-Warshall, A* |
| **MST** | 17, 18, 19 | Union-Find, Kruskal, Prim |
| **Connectivity** | 20 | Tarjan SCC |
| **Flow** | 21 | Ford-Fulkerson (max flow) |
| **Grid Problems** | 13, 22, 23 | Number of Islands, Flood Fill, Multi-Source BFS |

## All Files

| # | File | Content |
|---|------|---------|
| 01 | `01_adjacency_list.py` | Simple graph as dict |
| 02 | `02_class.py` | Graph as class |
| 03 | `03_bfs.py` | Breadth-First Search |
| 04 | `04_dfs.py` | Depth-First Search |
| 05 | `05_adjacency_list.py` | Full adjacency list (BFS, DFS) |
| 06 | `06_adjacency_matrix.py` | Adjacency matrix |
| 07 | `07_path_search.py` | Path search, connected components |
| 08 | `08_dijkstra.py` | Dijkstra shortest path |
| 09 | `09_cycle_detection.py` | Cycle detection |
| 10 | `10_topological_sort.py` | Topological sort (Kahn) |
| 11 | `11_weighted_complete.py` | Weighted graph |
| 12 | `12_summary.py` | Summary |
| 13 | `13_number_of_islands.py` | Number of Islands (LeetCode 200) |
| 14 | `14_bellman_ford.py` | Bellman-Ford (negative weights) |
| 15 | `15_floyd_warshall.py` | Floyd-Warshall (all-pairs) |
| 16 | `16_a_star.py` | A* pathfinding |
| 17 | `17_union_find.py` | Union-Find (disjoint set) |
| 18 | `18_kruskal.py` | Kruskal MST |
| 19 | `19_prim.py` | Prim MST |
| 20 | `20_tarjan_scc.py` | Tarjan strongly connected components |
| 21 | `21_ford_fulkerson.py` | Ford-Fulkerson max flow |
| 22 | `22_flood_fill.py` | Flood Fill (LeetCode 733) |
| 23 | `23_multi_source_bfs.py` | Multi-Source BFS (e.g. rotting oranges) |
| — | `adjacency_list.py` | Helper (re-exports GrafoListaAdyacencia) |

## Run

```bash
cd 15_Graphs
python 08_dijkstra.py
python 14_bellman_ford.py
python 18_kruskal.py
python 22_flood_fill.py
# ... etc.
```

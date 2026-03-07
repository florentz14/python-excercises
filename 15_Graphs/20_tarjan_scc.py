"""
15_Graphs - Tarjan's Strongly Connected Components (SCC)
==========================================================
Finds all SCCs in a directed graph using one DFS pass.
Used in: compilers, deadlock detection, social networks.
"""

from collections import defaultdict


def tarjan_scc(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    """
    Returns list of SCCs (each SCC is a list of node indices).
    edges: [(u, v), ...] directed.
    """
    adj: dict[int, list[int]] = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    index_counter = [0]
    stack = []
    low = {}
    index = {}
    on_stack = {}
    sccs = []

    def strongconnect(v):
        index[v] = index_counter[0]
        low[v] = index_counter[0]
        index_counter[0] += 1
        stack.append(v)
        on_stack[v] = True

        for w in adj[v]:
            if w not in index:
                strongconnect(w)
                low[v] = min(low[v], low[w])
            elif on_stack.get(w):
                low[v] = min(low[v], index[w])

        if low[v] == index[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for i in range(n):
        if i not in index:
            strongconnect(i)

    return sccs


if __name__ == "__main__":
    print("=== Tarjan SCC ===\n")
    # Directed graph: 0->1, 1->2, 2->0, 1->3, 3->4, 4->3
    edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 3)]
    sccs = tarjan_scc(5, edges)
    print(f"Strongly Connected Components: {sccs}")

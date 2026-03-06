# -------------------------------------------------
# File Name: 27_combinaciones_backtracking.py
# Author: Florentino Báez
# Date: Data Structures - Backtracking
# Description: Combination Generation with Backtracking.
#              Generates all ways to choose k elements from
#              a list regardless of order. Uses a start index
#              to avoid duplicates and builds subsets
#              incrementally, backtracking when completing each.
#              Complexity: O(C(n,k) * k).
# -------------------------------------------------

print("=== 5. Generación de Combinaciones (Backtracking) ===\n")


def combinaciones_backtracking(elements, k):
    """Generate all combinations of k elements using backtracking."""
    resultado = []
    n = len(elements)

    def backtrack(combinacion_actual, inicio):
        if len(combinacion_actual) == k:
            # Complete combination → save copy
            resultado.append(combinacion_actual[:])
            return
        # Only consider elements from 'inicio' to avoid duplicates
        for i in range(inicio, n):
            combinacion_actual.append(elements[i])     # Include element
            backtrack(combinacion_actual, i + 1)        # Next from i+1
            combinacion_actual.pop()                    # Backtrack: exclude

    backtrack([], 0)
    return resultado


if __name__ == "__main__":
    elementos_comb = ['A', 'B', 'C', 'D']
    k = 2
    combs = combinaciones_backtracking(elementos_comb, k)
    print(f"Combinaciones de {elementos_comb} tomando {k} elementos:")
    for i, comb in enumerate(combs, 1):
        print(f"  {i}. {comb}")
    print(f"Total: {len(combs)} combinaciones (C({len(elementos_comb)}, {k}) = {len(combs)})")

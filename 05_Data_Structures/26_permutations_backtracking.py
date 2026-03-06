# -------------------------------------------------
# File Name: 26_permutaciones_backtracking.py
# Author: Florentino Báez
# Date: Data Structures - Backtracking
# Description: Permutation Generation with Backtracking.
#              Generates all possible orderings of a list.
#              Uses a boolean array to track elements already
#              used and builds permutations element by element,
#              backtracking when exploring each branch.
#              Complexity: O(n! * n) generates n! permutations.
# -------------------------------------------------

print("=== 4. Generación de Permutaciones (Backtracking) ===\n")


def permutaciones_backtracking(elements):
    """Generate all permutations using backtracking."""
    resultado = []
    n = len(elements)

    def backtrack(permutacion_actual, usados):
        if len(permutacion_actual) == n:
            # Complete permutation → save copy
            resultado.append(permutacion_actual[:])
            return
        for i in range(n):
            if not usados[i]:
                permutacion_actual.append(elements[i])  # Choose element
                usados[i] = True                         # Mark as used
                backtrack(permutacion_actual, usados)     # Recursion
                permutacion_actual.pop()                  # Backtrack: remove
                usados[i] = False                         # Unmark

    backtrack([], [False] * n)
    return resultado


if __name__ == "__main__":
    elementos = [1, 2, 3]
    perms = permutaciones_backtracking(elementos)
    print(f"Permutaciones de {elementos}:")
    for i, perm in enumerate(perms, 1):
        print(f"  {i}. {perm}")
    print(f"Total: {len(perms)} permutaciones")

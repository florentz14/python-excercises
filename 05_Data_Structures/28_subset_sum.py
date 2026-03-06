# -------------------------------------------------
# File Name: 28_subset_sum.py
# Author: Florentino Báez
# Date: Data Structures - Backtracking
# Description: Subset Sum Problem.
#              Finds all subsets of a list of numbers
#              whose sum equals exactly the target.
#              For each element decides to include or exclude it,
#              pruning branches where the sum already exceeds target.
#              Complexity: O(2^n) in the worst case.
# -------------------------------------------------

print("=== 6. Problema de Suma de Subconjuntos (Subset Sum) ===\n")


def subset_sum_backtracking(numeros, objetivo):
    """Find subsets that sum exactly to the target."""
    resultado = []
    n = len(numeros)

    def backtrack(subconjunto_actual, indice, suma_actual):
        if suma_actual == objetivo:
            # Target sum reached → save subset
            resultado.append(subconjunto_actual[:])
            return
        if suma_actual > objetivo or indice >= n:
            return  # Prune: sum exceeded or no elements left
        # Option 1: Include current element
        subconjunto_actual.append(numeros[indice])
        backtrack(subconjunto_actual, indice + 1, suma_actual + numeros[indice])
        # Option 2: Exclude current element (backtrack)
        subconjunto_actual.pop()
        backtrack(subconjunto_actual, indice + 1, suma_actual)

    backtrack([], 0, 0)
    return resultado


if __name__ == "__main__":
    numeros_subset = [3, 34, 4, 12, 5, 2]
    objetivo_subset = 9
    soluciones_subset = subset_sum_backtracking(numeros_subset, objetivo_subset)

    print(f"Números: {numeros_subset}")
    print(f"Objetivo: {objetivo_subset}")
    print(f"Subconjuntos que suman {objetivo_subset}:")
    for sol in soluciones_subset:
        print(f"  {sol} (suma = {sum(sol)})")

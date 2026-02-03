# Archivo: 47_06_subset_sum.py
# Descripción: Problema de suma de subconjuntos (Subset Sum, backtracking)

print("=== 6. Problema de Suma de Subconjuntos (Subset Sum) ===\n")


def subset_sum_backtracking(numeros, objetivo):
    """Encuentra subconjuntos que sumen exactamente el objetivo."""
    resultado = []
    n = len(numeros)

    def backtrack(subconjunto_actual, indice, suma_actual):
        if suma_actual == objetivo:
            resultado.append(subconjunto_actual[:])
            return
        if suma_actual > objetivo or indice >= n:
            return
        subconjunto_actual.append(numeros[indice])
        backtrack(subconjunto_actual, indice + 1, suma_actual + numeros[indice])
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

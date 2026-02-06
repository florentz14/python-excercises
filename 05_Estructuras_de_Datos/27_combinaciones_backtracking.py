# Archivo: 47_05_combinaciones_backtracking.py
# Descripción: Generación de combinaciones con backtracking

print("=== 5. Generación de Combinaciones (Backtracking) ===\n")


def combinaciones_backtracking(elements, k):
    """Genera todas las combinaciones de k elementos usando backtracking."""
    resultado = []
    n = len(elements)

    def backtrack(combinacion_actual, inicio):
        if len(combinacion_actual) == k:
            resultado.append(combinacion_actual[:])
            return
        for i in range(inicio, n):
            combinacion_actual.append(elements[i])
            backtrack(combinacion_actual, i + 1)
            combinacion_actual.pop()

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

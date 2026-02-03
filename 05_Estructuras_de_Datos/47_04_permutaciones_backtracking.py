# Archivo: 47_04_permutaciones_backtracking.py
# Descripción: Generación de permutaciones con backtracking

print("=== 4. Generación de Permutaciones (Backtracking) ===\n")


def permutaciones_backtracking(elements):
    """Genera todas las permutaciones usando backtracking."""
    resultado = []
    n = len(elements)

    def backtrack(permutacion_actual, usados):
        if len(permutacion_actual) == n:
            resultado.append(permutacion_actual[:])
            return
        for i in range(n):
            if not usados[i]:
                permutacion_actual.append(elements[i])
                usados[i] = True
                backtrack(permutacion_actual, usados)
                permutacion_actual.pop()
                usados[i] = False

    backtrack([], [False] * n)
    return resultado


if __name__ == "__main__":
    elementos = [1, 2, 3]
    perms = permutaciones_backtracking(elementos)
    print(f"Permutaciones de {elementos}:")
    for i, perm in enumerate(perms, 1):
        print(f"  {i}. {perm}")
    print(f"Total: {len(perms)} permutaciones")

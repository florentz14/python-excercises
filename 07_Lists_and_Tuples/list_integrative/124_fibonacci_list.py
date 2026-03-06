# ---------------------------------------------------------------------------
# 265. Generate Fibonacci List (first n terms)
# ---------------------------------------------------------------------------
# Descripción: Genera una lista con los primeros n términos de la sucesión
#              de Fibonacci (cada término es la suma de los dos anteriores).
# Entrada: n (cantidad de términos, entero).
# Salida: Lista [0, 1, 1, 2, 3, 5, 8, ...].
# ---------------------------------------------------------------------------

def fibonacci_list(n: int) -> list[int]:
    # Casos especiales: sin términos o solo el primero
    if n <= 0:
        return []
    if n == 1:
        return [0]
    # Empezamos con los dos primeros: 0 y 1
    fib = [0, 1]
    # A partir del tercer término: cada uno es la suma de los dos últimos
    for _ in range(2, n):
        # fib[-1] = último elemento, fib[-2] = penúltimo; append añade al final
        fib.append(fib[-1] + fib[-2])
    return fib


# --- Ejemplo de uso ---
print(fibonacci_list(7))   # [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_list(15))

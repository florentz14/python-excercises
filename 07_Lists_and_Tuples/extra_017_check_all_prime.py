# ---------------------------------------------------------------------------
# 17. Check If All Numbers Are Prime
# ---------------------------------------------------------------------------
# Descripción: Comprueba si todos los números de una lista son primos.
#              Devuelve False si alguno no lo es (incl. 0, 1 o compuestos).
# ---------------------------------------------------------------------------

def is_prime(n: int) -> bool:
    # Los números menores que 2 no se consideran primos
    if n < 2:
        return False
    # Solo hace falta comprobar divisores hasta la raíz cuadrada de n
    for i in range(2, int(n ** 0.5) + 1):
        # Si n es divisible por i, no es primo
        if n % i == 0:
            return False
    # No se encontró ningún divisor; es primo
    return True


def all_prime(lst: list[int]) -> bool:
    # all() devuelve True solo si is_prime(x) es True para cada x de la lista
    return all(is_prime(x) for x in lst)


# --- Ejemplo de uso ---
print(all_prime([0, 3, 4, 7, 9]))   # False (0 y 4 y 9 no son primos)
print(all_prime([3, 5, 7, 13]))     # True
print(all_prime([1, 5, 3]))         # False (1 no es primo)

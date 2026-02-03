#!/usr/bin/env python3
# -------------------------------------------------
# Verifica si un número es primo e imprime la lista
# de números primos hasta el número capturado.
# -------------------------------------------------


def es_primo(n: int) -> bool:
    """
    Verifica si un número es primo.
    Un número primo solo es divisible entre 1 y él mismo (ej: 2, 3, 5, 7).
    """
    # Los números menores que 2 no son primos (0, 1 y negativos)
    if n < 2:
        return False

    # Probamos divisores desde 2 hasta la raíz cuadrada de n (incluida).
    # range(2, int(n ** 0.5) + 1) significa:
    #   - 2: primer divisor posible (el 1 no cuenta)
    #   - n ** 0.5: raíz cuadrada de n (ej: 25 ** 0.5 = 5.0)
    #   - int(...): convertir a entero para el rango (ej: 5.0 → 5)
    #   - + 1: para incluir ese valor en range (range(2, 5) da 2,3,4; con +1 da 2,3,4,5)
    #
    # ¿Por qué solo hasta √n? Si n = a × b y a ≤ b, entonces a ≤ √n.
    # Si hubiera un divisor mayor que √n, el otro factor sería menor que √n
    # y ya lo habríamos encontrado. Así evitamos probar divisores innecesarios.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:  # % es el resto: si el resto es 0, i divide exactamente a n
            return False  # Encontramos un divisor → n no es primo
    return True  # No hubo divisores → n es primo


def primos_hasta(n: int) -> list[int]:
    """
    Devuelve la lista de números primos desde 2 hasta n (inclusive).
    Usa comprensión de listas: [valor for elemento in iterable if condición]
    """
    return [p for p in range(2, n + 1) if es_primo(p)]


def main() -> None:
    """Pide un número, indica si es primo y muestra todos los primos hasta ese número."""
    numero = int(input("Ingresa un número entero: "))

    if es_primo(numero):
        print(f"\n{numero} es un número primo.")
    else:
        print(f"\n{numero} no es un número primo.")

    lista_primos = primos_hasta(numero)
    print(f"\nNúmeros primos hasta {numero}:")
    print(lista_primos)


if __name__ == "__main__":
    main()

# -------------------------------------------------
# File Name: 05_cambio_monedas.py
# Author: Florentino Báez
# Date: Data Structures - Greedy Algorithms
# Description: Coin Change with Greedy Algorithm.
#              Calculates the minimum number of coins to make
#              change by always choosing the largest coin possible.
#              Only optimal for canonical coin systems (e.g. USD,
#              EUR). A counter-example is included.
#              Complexity: O(n) where n = number of coin types.
# -------------------------------------------------

print("=== 5. Cambio de Monedas (Algoritmo Greedy) ===\n")


def cambio_monedas_greedy(monedas, cantidad):
    """
    Makes change using a greedy algorithm.
    Only works for canonical coin systems (e.g. USD, EUR).
    Complexity: O(n)
    """
    # Sort coins from largest to smallest (greedy: use the biggest first)
    monedas = sorted(monedas, reverse=True)
    cambio = []              # List of (coin, quantity used)
    cantidad_restante = cantidad

    for moneda in monedas:
        if cantidad_restante >= moneda:
            cantidad_moneda = cantidad_restante // moneda  # How many fit
            cambio.append((moneda, cantidad_moneda))
            cantidad_restante -= cantidad_moneda * moneda  # Subtract the covered amount
        if cantidad_restante == 0:
            break  # Change is complete

    return cambio, cantidad_restante


if __name__ == "__main__":
    monedas_canonicas = [1, 5, 10, 25, 50, 100]
    cantidad_cambio = 287

    print(f"Monedas disponibles: {monedas_canonicas}")
    print(f"Cantidad a cambiar: {cantidad_cambio}")

    cambio, resto = cambio_monedas_greedy(monedas_canonicas, cantidad_cambio)
    print("\nCambio (moneda, cantidad):")
    total = 0
    for moneda, cantidad in cambio:
        print(f"  {moneda}: {cantidad} moneda(s)")
        total += moneda * cantidad
    print(f"Total: {total}")
    if resto > 0:
        print(f"Resto no cambiado: {resto}")

    print("\n[AVISO] Ejemplo donde Greedy NO es óptimo:")
    monedas_no_canonicas = [1, 3, 4]
    cantidad_falla = 6
    cambio_greedy, _ = cambio_monedas_greedy(monedas_no_canonicas, cantidad_falla)
    print(f"Monedas: {monedas_no_canonicas}, Cantidad: {cantidad_falla}")
    print(f"Greedy da: {sum(c for _, c in cambio_greedy)} monedas")
    print("Óptimo sería: 2 monedas (3+3)")

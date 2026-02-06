# Archivo: 42_05_cambio_monedas.py
# Descripción: Cambio de monedas (algoritmo greedy)

print("=== 5. Cambio de Monedas (Algoritmo Greedy) ===\n")


def cambio_monedas_greedy(monedas, cantidad):
    """
    Cambio usando algoritmo greedy.
    Solo funciona para sistemas de monedas canónicos (ej. USD, EUR).
    Complejidad: O(n)
    """
    monedas = sorted(monedas, reverse=True)
    cambio = []
    cantidad_restante = cantidad

    for moneda in monedas:
        if cantidad_restante >= moneda:
            cantidad_moneda = cantidad_restante // moneda
            cambio.append((moneda, cantidad_moneda))
            cantidad_restante -= cantidad_moneda * moneda
        if cantidad_restante == 0:
            break

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

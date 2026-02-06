# Archivo: 42_01_mochila_fraccionaria.py
# Descripción: Problema de la mochila fraccionaria (algoritmo greedy)

print("=== Algoritmos Greedy (Voraces) ===\n")
print("=== 1. Problema de la Mochila Fraccionaria ===\n")


def mochila_fraccionaria(pesos, valores, capacidad):
    """
    Resuelve el problema de la mochila fraccionaria usando algoritmo greedy.
    Estrategia: Tomar items con mayor valor/peso primero.
    Complejidad: O(n log n)
    """
    n = len(pesos)
    items = [(valores[i] / pesos[i], pesos[i], valores[i], i) for i in range(n)]
    items.sort(reverse=True)

    valor_total = 0
    peso_actual = 0
    solucion = []

    for ratio, peso, valor, indice in items:
        if peso_actual + peso <= capacidad:
            peso_actual += peso
            valor_total += valor
            solucion.append((indice, 1.0))
        else:
            fraccion = (capacidad - peso_actual) / peso
            peso_actual = capacidad
            valor_total += valor * fraccion
            solucion.append((indice, fraccion))
            break

    return valor_total, solucion


if __name__ == "__main__":
    pesos_mochila = [10, 20, 30]
    valores_mochila = [60, 100, 120]
    capacidad_mochila = 50

    print(f"Pesos: {pesos_mochila}")
    print(f"Valores: {valores_mochila}")
    print(f"Capacidad: {capacidad_mochila}")

    valor_optimo, solucion = mochila_fraccionaria(pesos_mochila, valores_mochila, capacidad_mochila)
    print(f"\nValor máximo: {valor_optimo}")
    print("Solución (índice, fracción):")
    for indice, fraccion in solucion:
        print(f"  Item {indice}: {fraccion*100:.1f}% (peso: {pesos_mochila[indice]*fraccion:.1f}, valor: {valores_mochila[indice]*fraccion:.1f})")

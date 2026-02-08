# -------------------------------------------------
# File Name: 01_mochila_fraccionaria.py
# Author: Florentino Báez
# Date: Data Structures - Greedy Algorithms
# Description: Fractional Knapsack Problem (Greedy).
#              Selects items by value/weight ratio to maximize
#              total value without exceeding capacity. Items can
#              be taken partially (fractionally).
#              Complexity: O(n log n) due to sorting.
# -------------------------------------------------

print("=== Algoritmos Greedy (Voraces) ===\n")
print("=== 1. Problema de la Mochila Fraccionaria ===\n")


def mochila_fraccionaria(pesos, valores, capacidad):
    """
    Solves the fractional knapsack problem using a greedy algorithm.
    Strategy: Take items with highest value/weight ratio first.
    Complexity: O(n log n)
    """
    n = len(pesos)
    # Create tuples (value/weight ratio, weight, value, index) for each item
    items = [(valores[i] / pesos[i], pesos[i], valores[i], i) for i in range(n)]
    # Sort by ratio from highest to lowest (greedy strategy)
    items.sort(reverse=True)

    valor_total = 0    # Accumulated value in the knapsack
    peso_actual = 0    # Accumulated weight in the knapsack
    solucion = []      # List of (index, fraction) for each selected item

    for ratio, peso, valor, indice in items:
        if peso_actual + peso <= capacidad:
            # The item fits entirely in the knapsack
            peso_actual += peso
            valor_total += valor
            solucion.append((indice, 1.0))  # Fraction 1.0 = whole item
        else:
            # Only a fraction of the item fits
            fraccion = (capacidad - peso_actual) / peso  # Calculate the fraction that fits
            peso_actual = capacidad                       # Knapsack is now full
            valor_total += valor * fraccion               # Add proportional value
            solucion.append((indice, fraccion))
            break  # Knapsack full, no more space

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

"""
05_Estructuras_de_Datos - Cocktail Sort (ordenamiento de coctelera)
====================================================================
También conocido como Cocktail Shaker Sort, Bidirectional Bubble Sort
o Ripple Sort. Es una variación del Bubble Sort que recorre la lista
en ambas direcciones (ida y vuelta).

Complejidad:
  - Peor caso:  O(n²)
  - Promedio:   O(n²)
  - Mejor caso: O(n) si ya está ordenada
  - Espacio:    O(1) - In-place
  - Estabilidad: SÍ es estable

Ventaja sobre Bubble Sort: evita el problema de los "conejos y tortugas"
(elementos pequeños al final tardan mucho en moverse con Bubble Sort
pero Cocktail Sort los mueve rápido en la pasada de vuelta).
"""

import random
import time


# ============================================================
# 1. Cocktail Sort básico
# ============================================================
def cocktail_sort(lista):
    """
    Cocktail Sort: Bubble Sort bidireccional.
    Recorre de izquierda a derecha y luego de derecha a izquierda.
    No modifica la lista original.
    """
    lista = lista.copy()
    n = len(lista)
    inicio = 0
    fin = n - 1
    intercambiado = True

    while intercambiado:
        intercambiado = False

        # Pasada de izquierda a derecha (burbujea el mayor al final)
        for i in range(inicio, fin):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambiado = True
        fin -= 1

        if not intercambiado:
            break

        intercambiado = False

        # Pasada de derecha a izquierda (burbujea el menor al inicio)
        for i in range(fin, inicio, -1):
            if lista[i] < lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                intercambiado = True
        inicio += 1

    return lista


# ============================================================
# 2. Cocktail Sort con visualización
# ============================================================
def cocktail_sort_visual(lista):
    """Cocktail Sort con visualización paso a paso."""
    lista = lista.copy()
    n = len(lista)
    inicio = 0
    fin = n - 1
    intercambiado = True
    paso = 0

    print(f"\nLista original: {lista}")
    print(f"{'='*60}")

    while intercambiado:
        intercambiado = False
        paso += 1

        # Izquierda -> Derecha
        for i in range(inicio, fin):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambiado = True
        fin -= 1
        print(f"Paso {paso}a (→ derecha): {lista}")

        if not intercambiado:
            break

        intercambiado = False

        # Derecha -> Izquierda
        for i in range(fin, inicio, -1):
            if lista[i] < lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                intercambiado = True
        inicio += 1
        print(f"Paso {paso}b (← izquierda): {lista}")

    print(f"{'='*60}")
    print(f"Lista ordenada: {lista}")
    return lista


# ============================================================
# 3. Comparación: Cocktail Sort vs Bubble Sort
# ============================================================
def bubble_sort(lista):
    """Bubble Sort para comparación."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
    return lista


def comparar_con_bubble(n=2000):
    """Compara Cocktail Sort vs Bubble Sort en diferentes escenarios."""
    escenarios = {
        "Aleatorio":      [random.randint(1, 10000) for _ in range(n)],
        "Casi ordenado":  list(range(n)),
        "Inverso":        list(range(n, 0, -1)),
    }

    # Desordenar un poco el "casi ordenado"
    casi = escenarios["Casi ordenado"]
    for _ in range(n // 20):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        casi[i], casi[j] = casi[j], casi[i]

    print(f"\nCocktail Sort vs Bubble Sort ({n} elementos):")
    print("=" * 60)
    print(f"{'Escenario':<18s} {'Cocktail':>12s} {'Bubble':>12s} {'Ganador':>10s}")
    print("-" * 60)

    for nombre, datos in escenarios.items():
        inicio = time.time()
        cocktail_sort(datos)
        t_cocktail = time.time() - inicio

        inicio = time.time()
        bubble_sort(datos)
        t_bubble = time.time() - inicio

        ganador = "Cocktail" if t_cocktail < t_bubble else "Bubble"
        print(f"  {nombre:<18s} {t_cocktail*1000:10.2f} ms {t_bubble*1000:10.2f} ms"
              f" {ganador:>10s}")


# ============================================================
# 4. Contar intercambios y pasadas
# ============================================================
def cocktail_sort_stats(lista):
    """Cocktail Sort que cuenta intercambios y pasadas."""
    lista = lista.copy()
    n = len(lista)
    inicio = 0
    fin = n - 1
    intercambiado = True
    total_swaps = 0
    total_pasadas = 0

    while intercambiado:
        intercambiado = False
        total_pasadas += 1

        for i in range(inicio, fin):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambiado = True
                total_swaps += 1
        fin -= 1

        if not intercambiado:
            break

        intercambiado = False
        total_pasadas += 1

        for i in range(fin, inicio, -1):
            if lista[i] < lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                intercambiado = True
                total_swaps += 1
        inicio += 1

    return lista, total_pasadas, total_swaps


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Cocktail Sort (Bidirectional Bubble Sort) ===\n")

    # Demo visual
    lista_demo = [5, 1, 4, 2, 8, 0, 2, 7, 3, 6]
    cocktail_sort_visual(lista_demo)

    # Estadísticas
    print("\n--- Estadísticas de intercambios ---")
    casos_stats = {
        "Aleatorio":  [random.randint(1, 50) for _ in range(15)],
        "Inverso":    list(range(10, 0, -1)),
        "Ordenado":   list(range(1, 11)),
    }

    for nombre, caso in casos_stats.items():
        resultado, pasadas, swaps = cocktail_sort_stats(caso)
        print(f"  {nombre:12s}: {pasadas:3d} pasadas, {swaps:3d} intercambios"
              f" -> {resultado[:8]}{'...' if len(resultado) > 8 else ''}")

    # Pruebas de funcionamiento
    print("\n--- Pruebas ---")
    casos = {
        "Aleatoria":     [random.randint(1, 50) for _ in range(15)],
        "Ya ordenada":   list(range(1, 11)),
        "Inversa":       list(range(10, 0, -1)),
        "Iguales":       [5] * 8,
        "Un elemento":   [42],
        "Vacía":         [],
    }

    for nombre, caso in casos.items():
        resultado = cocktail_sort(caso)
        ok = all(resultado[i] <= resultado[i + 1]
                 for i in range(len(resultado) - 1)) if len(resultado) > 1 else True
        print(f"  {nombre:15s}: {caso[:8]}{'...' if len(caso) > 8 else ''}"
              f" -> {resultado[:8]}{'...' if len(resultado) > 8 else ''}"
              f" {'OK' if ok else 'FAIL'}")

    # Comparación
    comparar_con_bubble(1500)

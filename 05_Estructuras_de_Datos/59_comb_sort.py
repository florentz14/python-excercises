"""
05_Estructuras_de_Datos - Comb Sort (ordenamiento de peine)
=============================================================
Mejora del Bubble Sort que utiliza un gap (peine) que se reduce
progresivamente. Similar en concepto al Shell Sort pero aplicado
a la mecánica de Bubble Sort.

Complejidad:
  - Peor caso:  O(n²)
  - Promedio:   O(n² / 2^p) donde p = número de incrementos
  - Mejor caso: O(n log n)
  - Espacio:    O(1) - In-place
  - Estabilidad: NO es estable

Factor de reducción: 1.3 (valor óptimo encontrado empíricamente).
Cuando el gap llega a 1, se convierte en un Bubble Sort estándar.

Ventaja: Elimina las "tortugas" (valores pequeños al final) que
hacen lento al Bubble Sort, similar a cómo Shell Sort mejora
el Insertion Sort.
"""

import random
import time


# ============================================================
# 1. Comb Sort básico
# ============================================================
def comb_sort(lista):
    """
    Comb Sort: Bubble Sort con gaps decrecientes.
    Factor de reducción: 1.3 (óptimo).
    No modifica la lista original.
    """
    lista = lista.copy()
    n = len(lista)
    gap = n
    factor = 1.3  # Factor de reducción (shrink factor)
    intercambiado = True

    while gap > 1 or intercambiado:
        # Calcular el nuevo gap
        gap = max(1, int(gap / factor))
        intercambiado = False

        # Comparar e intercambiar elementos a distancia 'gap'
        for i in range(n - gap):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                intercambiado = True

    return lista


# ============================================================
# 2. Comb Sort con "regla del 11"
# ============================================================
def comb_sort_11(lista):
    """
    Comb Sort con la optimización "Comb Sort 11":
    Si el gap es 9 o 10, se fuerza a 11. Esto mejora el rendimiento
    porque evita ciertos patrones que causan mal desempeño.
    """
    lista = lista.copy()
    n = len(lista)
    gap = n
    factor = 1.3
    intercambiado = True

    while gap > 1 or intercambiado:
        gap = max(1, int(gap / factor))

        # Optimización: si gap es 9 o 10, usar 11
        if gap == 9 or gap == 10:
            gap = 11

        intercambiado = False

        for i in range(n - gap):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                intercambiado = True

    return lista


# ============================================================
# 3. Comb Sort con visualización
# ============================================================
def comb_sort_visual(lista):
    """Comb Sort con visualización del proceso."""
    lista = lista.copy()
    n = len(lista)
    gap = n
    factor = 1.3
    intercambiado = True
    paso = 0

    print(f"\nLista original: {lista}")
    print(f"{'='*60}")

    while gap > 1 or intercambiado:
        gap = max(1, int(gap / factor))
        intercambiado = False
        swaps = 0
        paso += 1

        for i in range(n - gap):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                intercambiado = True
                swaps += 1

        print(f"Paso {paso:2d} (gap={gap:2d}): {lista}  ({swaps} swaps)")

    print(f"{'='*60}")
    print(f"Lista ordenada: {lista}")
    return lista


# ============================================================
# 4. Comparación de factores de reducción
# ============================================================
def comparar_factores(n=5000):
    """Compara diferentes factores de reducción."""
    lista = [random.randint(1, 10000) for _ in range(n)]

    print(f"\nComparación de factores de reducción ({n} elementos):")
    print("=" * 50)

    def comb_con_factor(lista, factor):
        lista = lista.copy()
        n = len(lista)
        gap = n
        intercambiado = True
        while gap > 1 or intercambiado:
            gap = max(1, int(gap / factor))
            intercambiado = False
            for i in range(n - gap):
                if lista[i] > lista[i + gap]:
                    lista[i], lista[i + gap] = lista[i + gap], lista[i]
                    intercambiado = True
        return lista

    for factor in [1.1, 1.2, 1.3, 1.4, 1.5, 2.0]:
        copia = lista.copy()
        inicio = time.time()
        resultado = comb_con_factor(copia, factor)
        tiempo = time.time() - inicio
        ok = all(resultado[i] <= resultado[i + 1]
                 for i in range(len(resultado) - 1))
        print(f"  Factor {factor:.1f}: {tiempo*1000:8.2f} ms {'OK' if ok else 'FAIL'}")

    print("\nEl factor 1.3 es generalmente el mejor.")


# ============================================================
# 5. Comparación con Bubble Sort y Shell Sort
# ============================================================
def bubble_sort(lista):
    """Bubble Sort optimizado para comparación."""
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


def shell_sort(lista):
    """Shell Sort para comparación."""
    lista = lista.copy()
    n = len(lista)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista


def comparar(n=3000):
    """Compara Comb Sort con Bubble Sort y Shell Sort."""
    lista = [random.randint(1, 10000) for _ in range(n)]

    metodos = {
        "Bubble Sort":   bubble_sort,
        "Comb Sort":     comb_sort,
        "Comb Sort 11":  comb_sort_11,
        "Shell Sort":    shell_sort,
    }

    print(f"\nComparación ({n} elementos aleatorios):")
    print("=" * 50)

    for nombre, metodo in metodos.items():
        copia = lista.copy()
        inicio = time.time()
        resultado = metodo(copia)
        tiempo = time.time() - inicio
        ok = all(resultado[i] <= resultado[i + 1]
                 for i in range(len(resultado) - 1))
        print(f"  {nombre:15s}: {tiempo*1000:8.2f} ms {'OK' if ok else 'FAIL'}")

    print("\nComb Sort es mucho más rápido que Bubble Sort,")
    print("y comparable a Shell Sort en rendimiento.")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Comb Sort ===\n")

    # Demo visual
    lista_demo = [8, 4, 1, 56, 3, 78, 45, 23, 12, 64]
    comb_sort_visual(lista_demo)

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
        resultado = comb_sort(caso)
        ok = all(resultado[i] <= resultado[i + 1]
                 for i in range(len(resultado) - 1)) if len(resultado) > 1 else True
        print(f"  {nombre:15s}: {caso[:8]}{'...' if len(caso) > 8 else ''}"
              f" -> {resultado[:8]}{'...' if len(resultado) > 8 else ''}"
              f" {'OK' if ok else 'FAIL'}")

    # Comparaciones
    comparar_factores(3000)
    comparar(2000)

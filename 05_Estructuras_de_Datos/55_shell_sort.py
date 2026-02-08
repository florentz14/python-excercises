"""
05_Estructuras_de_Datos - Shell Sort (ordenamiento de Shell)
=============================================================
Inventado por Donald Shell (1959). Es una generalización del Insertion Sort
que permite intercambiar elementos distantes, reduciendo progresivamente
la brecha (gap) hasta que sea 1 (donde se convierte en Insertion Sort).

Complejidad:
  - Peor caso:  O(n²) con gaps de Shell, O(n^(3/2)) con gaps de Knuth
  - Promedio:   Depende de la secuencia de gaps
  - Mejor caso: O(n log n)
  - Espacio:    O(1) - In-place
  - Estabilidad: NO es estable

Secuencias de gaps comunes:
  - Shell:   n/2, n/4, ..., 1
  - Knuth:   1, 4, 13, 40, 121, ...  (3^k - 1) / 2
  - Hibbard: 1, 3, 7, 15, 31, ...    2^k - 1
  - Sedgewick: secuencias intercaladas

Ventaja sobre Insertion Sort: mueve elementos lejanos rápidamente.
"""

import time
import random


# ============================================================
# 1. Shell Sort - Secuencia de Shell (n/2)
# ============================================================
def shell_sort(lista):
    """
    Shell Sort con secuencia de gaps de Shell: n/2, n/4, ..., 1
    No modifica la lista original.
    """
    lista = lista.copy()
    n = len(lista)
    gap = n // 2  # Gap inicial

    while gap > 0:
        # Insertion Sort con el gap actual
        for i in range(gap, n):
            temp = lista[i]
            j = i
            # Mover elementos que están a distancia 'gap'
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2  # Reducir el gap

    return lista


# ============================================================
# 2. Shell Sort - Secuencia de Knuth
# ============================================================
def shell_sort_knuth(lista):
    """
    Shell Sort con secuencia de gaps de Knuth: 1, 4, 13, 40, 121, ...
    Fórmula: gap = (3^k - 1) / 2
    Mejor rendimiento que la secuencia de Shell.
    """
    lista = lista.copy()
    n = len(lista)

    # Calcular el gap inicial de Knuth (el mayor que sea < n/3)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1  # 1, 4, 13, 40, 121, 364, ...

    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 3  # Reducir usando secuencia inversa de Knuth

    return lista


# ============================================================
# 3. Shell Sort - Secuencia de Hibbard
# ============================================================
def shell_sort_hibbard(lista):
    """
    Shell Sort con secuencia de gaps de Hibbard: 1, 3, 7, 15, 31, ...
    Fórmula: 2^k - 1
    Complejidad peor caso: O(n^(3/2))
    """
    lista = lista.copy()
    n = len(lista)

    # Generar secuencia de Hibbard
    gaps = []
    k = 1
    while (2**k - 1) < n:
        gaps.append(2**k - 1)
        k += 1

    # Recorrer gaps de mayor a menor
    for gap in reversed(gaps):
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp

    return lista


# ============================================================
# 4. Visualización paso a paso
# ============================================================
def shell_sort_visual(lista):
    """Shell Sort con visualización de cada paso del gap."""
    lista = lista.copy()
    n = len(lista)
    gap = n // 2
    paso = 0

    print(f"\nLista original: {lista}")
    print(f"{'='*60}")

    while gap > 0:
        paso += 1
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp

        print(f"Paso {paso} (gap={gap}): {lista}")
        gap //= 2

    print(f"{'='*60}")
    print(f"Lista ordenada: {lista}")
    return lista


# ============================================================
# 5. Comparación de secuencias de gaps
# ============================================================
def comparar_secuencias(n=5000):
    """Compara el rendimiento de diferentes secuencias de gaps."""
    lista = [random.randint(1, 10000) for _ in range(n)]

    secuencias = {
        "Shell (n/2)":  shell_sort,
        "Knuth":        shell_sort_knuth,
        "Hibbard":      shell_sort_hibbard,
    }

    print(f"\nComparación de secuencias de gaps ({n} elementos):")
    print("=" * 50)

    for nombre, metodo in secuencias.items():
        copia = lista.copy()
        inicio = time.time()
        resultado = metodo(copia)
        tiempo = time.time() - inicio
        ordenada = all(resultado[i] <= resultado[i + 1]
                       for i in range(len(resultado) - 1))
        estado = "OK" if ordenada else "FAIL"
        print(f"  {estado} {nombre:15s}: {tiempo*1000:8.2f} ms")


# ============================================================
# 6. Comparación Shell Sort vs Insertion Sort
# ============================================================
def insertion_sort(lista):
    """Insertion Sort para comparación."""
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


def comparar_con_insertion(n=3000):
    """Compara Shell Sort vs Insertion Sort."""
    lista = [random.randint(1, 10000) for _ in range(n)]

    metodos = {
        "Insertion Sort": insertion_sort,
        "Shell Sort":     shell_sort,
        "Shell (Knuth)":  shell_sort_knuth,
    }

    print(f"\nShell Sort vs Insertion Sort ({n} elementos):")
    print("=" * 50)

    for nombre, metodo in metodos.items():
        copia = lista.copy()
        inicio = time.time()
        metodo(copia)
        tiempo = time.time() - inicio
        print(f"  {nombre:20s}: {tiempo*1000:8.2f} ms")

    print("\nShell Sort es mucho más rápido que Insertion Sort")
    print("porque mueve elementos lejanos antes de refinar.")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Shell Sort ===\n")

    # Demostración visual con lista pequeña
    lista_demo = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    shell_sort_visual(lista_demo)

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
        resultado = shell_sort(caso)
        ok = all(resultado[i] <= resultado[i + 1]
                 for i in range(len(resultado) - 1)) if len(resultado) > 1 else True
        print(f"  {nombre:15s}: {caso[:8]}{'...' if len(caso) > 8 else ''}"
              f" -> {resultado[:8]}{'...' if len(resultado) > 8 else ''}"
              f" {'OK' if ok else 'FAIL'}")

    # Comparaciones
    comparar_secuencias(3000)
    comparar_con_insertion(3000)

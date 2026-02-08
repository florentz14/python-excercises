"""
05_Estructuras_de_Datos - Tim Sort
====================================
Inventado por Tim Peters (2002) para Python. Es el algoritmo detrás de
sorted() y list.sort() en Python (y también en Java desde JDK 7).

Es un híbrido de Merge Sort e Insertion Sort que aprovecha las
"corridas" (runs) naturales en los datos del mundo real.

Complejidad:
  - Peor caso:  O(n log n)
  - Promedio:   O(n log n)
  - Mejor caso: O(n) cuando los datos ya están parcialmente ordenados
  - Espacio:    O(n)
  - Estabilidad: SÍ es estable

Conceptos clave:
  - RUN: Secuencia consecutiva ya ordenada (ascendente o descendente)
  - minrun: Tamaño mínimo de un run (típicamente 32-64)
  - Si un run es < minrun, se extiende con Insertion Sort
  - Los runs se combinan con un Merge optimizado

Tim Sort es EXCELENTE con datos parcialmente ordenados,
que es muy común en la vida real.
"""

import random
import time


# ============================================================
# 1. Calcular el minrun óptimo
# ============================================================
MIN_MERGE = 32


def calc_min_run(n):
    """
    Calcula el tamaño mínimo de un run.
    Retorna un valor entre 32 y 64 tal que n/minrun es cercano
    a una potencia de 2 (para merges eficientes).
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


# ============================================================
# 2. Insertion Sort para runs pequeños
# ============================================================
def insertion_sort_range(arr, left, right):
    """Insertion Sort in-place en el rango [left, right]."""
    for i in range(left + 1, right + 1):
        clave = arr[i]
        j = i - 1
        while j >= left and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave


# ============================================================
# 3. Merge de dos runs adyacentes
# ============================================================
def merge_runs(arr, left, mid, right):
    """
    Combina dos runs ordenados: arr[left..mid] y arr[mid+1..right].
    Optimizado: solo copia el lado más pequeño al buffer temporal.
    """
    len_left = mid - left + 1
    len_right = right - mid

    # Copiar a arrays temporales
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:  # <= para estabilidad
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1


# ============================================================
# 4. Tim Sort - Implementación
# ============================================================
def tim_sort(lista):
    """
    Tim Sort: híbrido de Merge Sort + Insertion Sort.
    No modifica la lista original.
    """
    arr = lista.copy()
    n = len(arr)

    if n <= 1:
        return arr

    min_run = calc_min_run(n)

    # Paso 1: Crear runs de tamaño min_run usando Insertion Sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_range(arr, start, end)

    # Paso 2: Mergear runs, duplicando el tamaño en cada iteración
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                merge_runs(arr, left, mid, right)

        size *= 2

    return arr


# ============================================================
# 5. Demostración: Tim Sort vs datos parcialmente ordenados
# ============================================================
def demostrar_ventaja():
    """Muestra la ventaja de Tim Sort con datos parcialmente ordenados."""
    n = 5000

    tipos_datos = {
        "Aleatorio":           [random.randint(1, 10000) for _ in range(n)],
        "Casi ordenado":       list(range(n)),  # Se desordena abajo
        "Bloques ordenados":   [],              # Se construye abajo
        "Pocos únicos":        [random.choice(range(10)) for _ in range(n)],
        "Inversamente ord.":   list(range(n, 0, -1)),
    }

    # Casi ordenado: intercambiar 5% de elementos
    casi = tipos_datos["Casi ordenado"]
    for _ in range(n // 20):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        casi[i], casi[j] = casi[j], casi[i]

    # Bloques ordenados: 10 bloques ya ordenados, concatenados desordenados
    bloques = []
    for _ in range(10):
        bloque = sorted([random.randint(1, 10000) for _ in range(n // 10)])
        bloques.extend(bloque)
    tipos_datos["Bloques ordenados"] = bloques

    print(f"\nRendimiento de Tim Sort vs sorted() ({n} elementos):")
    print("=" * 65)
    print(f"{'Tipo de datos':<22s} {'Tim Sort':>12s} {'sorted()':>12s}")
    print("-" * 65)

    for nombre, datos in tipos_datos.items():
        # Tim Sort
        copia1 = datos.copy()
        inicio = time.time()
        tim_sort(copia1)
        t_tim = time.time() - inicio

        # Python sorted()
        copia2 = datos.copy()
        inicio = time.time()
        sorted(copia2)
        t_python = time.time() - inicio

        print(f"  {nombre:<22s} {t_tim*1000:10.2f} ms {t_python*1000:10.2f} ms")


# ============================================================
# 6. Explicación visual del proceso
# ============================================================
def tim_sort_visual(lista):
    """Muestra el proceso de Tim Sort paso a paso."""
    arr = lista.copy()
    n = len(arr)
    min_run = calc_min_run(n)

    print(f"\nTim Sort paso a paso")
    print(f"Lista original: {arr}")
    print(f"n = {n}, min_run = {min_run}")
    print(f"{'='*60}")

    # Paso 1: Crear runs
    print(f"\nPaso 1 - Crear runs (Insertion Sort en bloques de {min_run}):")
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        before = arr[start:end + 1].copy()
        insertion_sort_range(arr, start, end)
        after = arr[start:end + 1]
        print(f"  [{start}:{end+1}] {before} -> {after}")

    # Paso 2: Merge
    print(f"\nPaso 2 - Merge de runs:")
    size = min_run
    paso = 0
    while size < n:
        paso += 1
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                print(f"  Merge [{left}:{mid+1}] + [{mid+1}:{right+1}]", end="")
                merge_runs(arr, left, mid, right)
                print(f" -> {arr[left:right+1]}")
        size *= 2

    print(f"\n{'='*60}")
    print(f"Resultado: {arr}")
    return arr


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Tim Sort ===\n")

    # Demo visual
    lista_demo = [5, 21, 7, 23, 19, 10, 42, 3, 15, 8, 31, 1, 27, 12]
    tim_sort_visual(lista_demo)

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
        resultado = tim_sort(caso)
        ok = all(resultado[i] <= resultado[i + 1]
                 for i in range(len(resultado) - 1)) if len(resultado) > 1 else True
        print(f"  {nombre:15s}: {caso[:8]}{'...' if len(caso) > 8 else ''}"
              f" -> {resultado[:8]}{'...' if len(resultado) > 8 else ''}"
              f" {'OK' if ok else 'FAIL'}")

    # Ventaja con datos parcialmente ordenados
    demostrar_ventaja()

    print("\nNota: sorted() y list.sort() de Python usan Tim Sort internamente.")
    print("Esta implementación es educativa; la versión de CPython está en C.")

"""
05_Estructuras_de_Datos - Bucket Sort (ordenamiento por cubetas)
=================================================================
Distribuye los elementos en cubetas (buckets), ordena cada cubeta
individualmente (con Insertion Sort u otro), y concatena los resultados.

Complejidad:
  - Peor caso:  O(n²) si todos los elementos caen en una cubeta
  - Promedio:   O(n + k) donde k = número de cubetas
  - Mejor caso: O(n + k) con distribución uniforme
  - Espacio:    O(n + k)
  - Estabilidad: SÍ es estable (si el sort interno es estable)

Ideal para: datos distribuidos uniformemente en un rango conocido,
            números en punto flotante entre [0, 1).
"""

import random
import time
import math


# ============================================================
# 1. Bucket Sort para flotantes [0, 1)
# ============================================================
def bucket_sort_float(lista):
    """
    Bucket Sort para números flotantes en rango [0, 1).
    Usa Insertion Sort dentro de cada cubeta.
    No modifica la lista original.
    """
    if len(lista) <= 1:
        return lista.copy()

    lista = lista.copy()
    n = len(lista)
    buckets = [[] for _ in range(n)]

    # Distribuir elementos en cubetas
    for num in lista:
        idx = int(n * num)  # Mapear [0, 1) a índice de cubeta
        if idx == n:        # Si num == 1.0, va en la última cubeta
            idx = n - 1
        buckets[idx].append(num)

    # Ordenar cada cubeta con Insertion Sort
    for bucket in buckets:
        insertion_sort_inplace(bucket)

    # Concatenar todas las cubetas
    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)

    return resultado


def insertion_sort_inplace(lista):
    """Insertion Sort in-place (para ordenar cubetas)."""
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave


# ============================================================
# 2. Bucket Sort para enteros (rango general)
# ============================================================
def bucket_sort_int(lista, num_buckets=None):
    """
    Bucket Sort para enteros con rango arbitrario.
    Distribuye basándose en el valor relativo al rango.
    """
    if len(lista) <= 1:
        return lista.copy()

    lista = lista.copy()
    min_val = min(lista)
    max_val = max(lista)

    if min_val == max_val:
        return lista  # Todos iguales

    n = len(lista)
    if num_buckets is None:
        num_buckets = max(1, int(math.sqrt(n)))

    rango = max_val - min_val + 1
    buckets = [[] for _ in range(num_buckets)]

    # Distribuir en cubetas
    for num in lista:
        idx = int((num - min_val) / rango * num_buckets)
        if idx == num_buckets:
            idx = num_buckets - 1
        buckets[idx].append(num)

    # Ordenar cada cubeta
    for bucket in buckets:
        insertion_sort_inplace(bucket)

    # Concatenar
    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)

    return resultado


# ============================================================
# 3. Bucket Sort con visualización
# ============================================================
def bucket_sort_visual(lista, num_buckets=5):
    """Bucket Sort con visualización del proceso."""
    if len(lista) <= 1:
        return lista.copy()

    lista = lista.copy()
    min_val = min(lista)
    max_val = max(lista)
    rango = max_val - min_val + 1

    buckets = [[] for _ in range(num_buckets)]

    print(f"\nLista original: {lista}")
    print(f"Rango: [{min_val}, {max_val}], Cubetas: {num_buckets}")
    print(f"{'='*60}")

    # Distribuir
    for num in lista:
        idx = int((num - min_val) / rango * num_buckets)
        if idx == num_buckets:
            idx = num_buckets - 1
        buckets[idx].append(num)

    print("\nDespués de distribuir:")
    for i, bucket in enumerate(buckets):
        rango_cubeta = (min_val + i * rango // num_buckets,
                        min_val + (i + 1) * rango // num_buckets - 1)
        print(f"  Cubeta {i} [{rango_cubeta[0]:3d}-{rango_cubeta[1]:3d}]: {bucket}")

    # Ordenar cada cubeta
    for bucket in buckets:
        insertion_sort_inplace(bucket)

    print("\nDespués de ordenar cada cubeta:")
    for i, bucket in enumerate(buckets):
        print(f"  Cubeta {i}: {bucket}")

    # Concatenar
    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)

    print(f"\n{'='*60}")
    print(f"Resultado: {resultado}")
    return resultado


# ============================================================
# 4. Bucket Sort para negativos
# ============================================================
def bucket_sort_negatives(lista):
    """
    Bucket Sort que maneja números negativos.
    Separa negativos y positivos, ordena por separado, une.
    """
    if len(lista) <= 1:
        return lista.copy()

    negativos = [-x for x in lista if x < 0]
    positivos = [x for x in lista if x >= 0]

    neg_sorted = bucket_sort_int(negativos) if negativos else []
    pos_sorted = bucket_sort_int(positivos) if positivos else []

    # Invertir negativos y negar de vuelta
    return [-x for x in reversed(neg_sorted)] + pos_sorted


# ============================================================
# 5. Comparación con otros algoritmos
# ============================================================
def comparar(n=5000):
    """Compara Bucket Sort con otros métodos."""
    # Datos uniformemente distribuidos (caso ideal para Bucket Sort)
    lista_float = [random.random() for _ in range(n)]
    lista_int = [random.randint(1, 10000) for _ in range(n)]

    print(f"\n--- Comparación con {n} flotantes uniformes [0, 1) ---")
    print("=" * 50)

    inicio = time.time()
    bucket_sort_float(lista_float)
    t_bucket = time.time() - inicio
    print(f"  Bucket Sort:     {t_bucket*1000:8.2f} ms")

    inicio = time.time()
    sorted(lista_float)
    t_sorted = time.time() - inicio
    print(f"  Python sorted(): {t_sorted*1000:8.2f} ms")

    print(f"\n--- Comparación con {n} enteros [1, 10000] ---")
    print("=" * 50)

    inicio = time.time()
    bucket_sort_int(lista_int)
    t_bucket_i = time.time() - inicio
    print(f"  Bucket Sort:     {t_bucket_i*1000:8.2f} ms")

    inicio = time.time()
    sorted(lista_int)
    t_sorted_i = time.time() - inicio
    print(f"  Python sorted(): {t_sorted_i*1000:8.2f} ms")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Bucket Sort ===\n")

    # Demo visual
    lista_demo = [29, 25, 3, 49, 9, 37, 21, 43, 15, 33]
    bucket_sort_visual(lista_demo, num_buckets=5)

    # Pruebas de flotantes
    print("\n--- Prueba flotantes [0, 1) ---")
    floats = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    resultado = bucket_sort_float(floats)
    print(f"  Original:  {floats}")
    print(f"  Ordenada:  {resultado}")

    # Pruebas con negativos
    print("\n--- Prueba con negativos ---")
    negativos = [5, -3, 8, -1, 0, -7, 3, -2, 6, -5]
    resultado_neg = bucket_sort_negatives(negativos)
    print(f"  Original:  {negativos}")
    print(f"  Ordenada:  {resultado_neg}")

    # Casos especiales
    print("\n--- Casos especiales ---")
    casos = {
        "Ya ordenada":  list(range(1, 11)),
        "Inversa":      list(range(10, 0, -1)),
        "Iguales":      [5] * 8,
        "Un elemento":  [42],
        "Vacía":        [],
    }
    for nombre, caso in casos.items():
        res = bucket_sort_int(caso) if caso else []
        ok = all(res[i] <= res[i + 1] for i in range(len(res) - 1)) if len(res) > 1 else True
        print(f"  {nombre:15s}: {caso} -> {res} {'OK' if ok else 'FAIL'}")

    # Comparación de rendimiento
    comparar(3000)

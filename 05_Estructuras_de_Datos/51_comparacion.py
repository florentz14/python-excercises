"""
05_Estructuras_de_Datos - Comparación de métodos de ordenamiento
=================================================================
Mide tiempos de cada algoritmo sobre la misma lista.
"""

import time
import random


# === Utilidades ===
def esta_ordenada(lista):
    """Verifica si una lista está ordenada de forma ascendente."""
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def generar_lista_aleatoria(n, minimo=1, maximo=100):
    """Genera una lista aleatoria de n elementos."""
    return [random.randint(minimo, maximo) for _ in range(n)]


# === Bubble Sort ===
def bubble_sort(lista):
    """Bubble sort clásico. No modifica la lista original."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def bubble_sort_optimizado(lista):
    """Se detiene si no hay intercambios (lista ya ordenada)."""
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


# === Selection Sort ===
def selection_sort(lista):
    """En cada paso coloca el mínimo del resto en la posición actual."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


# === Insertion Sort ===
def insertion_sort(lista):
    """Inserta cada elemento en su lugar dentro de la parte ya ordenada."""
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


# === Merge Sort ===
def merge(izquierda, derecha):
    """Combina dos listas ordenadas en una ordenada."""
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def merge_sort(lista):
    """Divide y vencerás: dividir, ordenar mitades, combinar."""
    if len(lista) <= 1:
        return lista.copy()
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)


# === Quick Sort ===
def quick_sort(lista):
    """Versión que usa listas auxiliares (clara). Pivote: elemento central."""
    if len(lista) <= 1:
        return lista.copy()
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)


# === Heap Sort ===
def heapify(lista, n, i):
    """Ajusta el árbol para que la raíz en i sea un heap máximo."""
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2
    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda
    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)


def heap_sort(lista):
    """Construye heap máximo y extrae el máximo repetidamente."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)
    return lista


# === Counting Sort ===
def counting_sort(lista, maximo=None):
    """Ordena contando ocurrencias de cada valor (enteros no negativos)."""
    if maximo is None:
        maximo = max(lista) if lista else 0
    count = [0] * (maximo + 1)
    for num in lista:
        count[num] += 1
    resultado = []
    for i in range(maximo + 1):
        resultado.extend([i] * count[i])
    return resultado


# === Comparación ===
def comparar_metodos_ordenamiento(lista, mostrar_resultados=True):
    """Compara tiempos de todos los métodos. No modifica la lista original."""
    metodos = {
        "Bubble Sort": bubble_sort,
        "Bubble Sort Optimizado": bubble_sort_optimizado,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
        "Python sorted()": sorted,
    }
    tiempos = {}
    print(f"\nComparando métodos para lista de {len(lista)} elementos:")
    print("=" * 70)
    for nombre, metodo in metodos.items():
        lista_copia = lista.copy()
        inicio = time.time()
        try:
            resultado = metodo(lista_copia)
            tiempo = time.time() - inicio
            ordenada = esta_ordenada(resultado)
            tiempos[nombre] = tiempo
            estado = "OK" if ordenada else "FAIL"
            print(f"{estado} {nombre:25s} {tiempo*1000:8.4f} ms")
        except Exception as e:
            print(f"ERR {nombre:25s} Error: {e}")
            tiempos[nombre] = float("inf")
    print("=" * 70)
    tiempos_validos = {k: v for k, v in tiempos.items() if v != float("inf")}
    if tiempos_validos:
        mas_rapido = min(tiempos_validos, key=tiempos_validos.get)
        print(f"\nMétodo más rápido: {mas_rapido} ({tiempos_validos[mas_rapido]*1000:.4f} ms)")
    return tiempos


if __name__ == "__main__":
    print("=== Comparación de métodos ===\n")
    print("Lista pequeña (10 elementos):")
    lista_peq = generar_lista_aleatoria(10, 1, 50)
    print(f"Lista: {lista_peq}")
    comparar_metodos_ordenamiento(lista_peq)
    print("\nLista mediana (100 elementos):")
    lista_med = generar_lista_aleatoria(100, 1, 100)
    comparar_metodos_ordenamiento(lista_med)

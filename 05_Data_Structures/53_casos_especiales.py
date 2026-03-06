# -------------------------------------------------
# File Name: 53_casos_especiales.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Special Cases of Sorting.
#              Tests Merge Sort with edge cases: already
#              sorted list, reverse sorted, all equal elements,
#              single element and empty list. Verifies that the
#              algorithm works correctly in all cases.
# -------------------------------------------------


def esta_ordenada(lista):
    """Checks if a list is sorted in ascending order."""
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def merge(izquierda, derecha):
    """Merges two sorted lists into one sorted list."""
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
    """Divide and conquer: divide, sort halves, merge."""
    if len(lista) <= 1:
        return lista.copy()
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)


def probar_casos_especiales():
    """Tests Merge Sort with different edge cases."""
    casos = {
        "Lista ya ordenada": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Lista inversamente ordenada": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "Lista con elementos iguales": [5, 5, 5, 5, 5, 5],
        "Lista con un elemento": [42],
        "Lista vacía": [],
    }
    print("\nCasos especiales (Merge Sort):")
    print("=" * 70)
    for nombre, lista in casos.items():
        print(f"\n{nombre}: {lista}")
        if lista:
            resultado = merge_sort(lista)
            print(f"  Ordenada: {resultado}")
            print(f"  Verificación: {'OK' if esta_ordenada(resultado) else 'FAIL'}")
        else:
            print("  Lista vacía - no se ordena")


if __name__ == "__main__":
    print("=== Casos especiales ===\n")
    probar_casos_especiales()

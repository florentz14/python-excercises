"""
05_Estructuras_de_Datos - Casos especiales de ordenamiento
==========================================================
Lista ya ordenada, inversa, iguales, un elemento, vacía.
"""


def esta_ordenada(lista):
    """Verifica si una lista está ordenada de forma ascendente."""
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


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


def probar_casos_especiales():
    """Prueba Merge Sort con distintos casos límite."""
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

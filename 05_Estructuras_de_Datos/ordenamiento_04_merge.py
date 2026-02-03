"""
05_Estructuras_de_Datos - Merge Sort (ordenamiento por mezcla)
==============================================================
Complejidad: O(n log n). Estable. No in-place (O(n) extra).
"""


def merge_sort(lista):
    """Divide y vencerás: dividir, ordenar mitades, combinar."""
    if len(lista) <= 1:
        return lista.copy()
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)


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


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Merge Sort:", merge_sort(ejemplo))

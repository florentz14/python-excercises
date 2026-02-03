"""
05_Estructuras_de_Datos - Counting Sort (ordenamiento por conteo)
==================================================================
Complejidad: O(n + k), k = rango. Estable. No in-place. Bueno para rango pequeño.
"""


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


if __name__ == "__main__":
    ejemplo = [4, 2, 2, 8, 3, 3, 1]
    print("Lista original:", ejemplo)
    print("Counting Sort:", counting_sort(ejemplo))

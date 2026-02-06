"""
05_Estructuras_de_Datos - Casos especiales de ordenamiento
==========================================================
Lista ya ordenada, inversa, iguales, un elemento, vacía.
"""

from ordenamiento_00_utilidades import esta_ordenada
from ordenamiento_04_merge import merge_sort


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

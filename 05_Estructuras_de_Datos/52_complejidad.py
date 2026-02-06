"""
05_Estructuras_de_Datos - Análisis de complejidad temporal
===========================================================
Tabla de mejor caso, promedio y peor caso por método.
"""


def analizar_complejidad():
    """Imprime tabla de complejidades."""
    print("\nComplejidad temporal de los métodos:")
    print("=" * 70)
    print(f"{'Método':<25} {'Mejor Caso':<15} {'Caso Promedio':<15} {'Peor Caso':<15}")
    print("-" * 70)
    datos = [
        ("Bubble Sort", "O(n)", "O(n²)", "O(n²)"),
        ("Bubble Sort Optimizado", "O(n)", "O(n²)", "O(n²)"),
        ("Selection Sort", "O(n²)", "O(n²)", "O(n²)"),
        ("Insertion Sort", "O(n)", "O(n²)", "O(n²)"),
        ("Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)"),
        ("Quick Sort", "O(n log n)", "O(n log n)", "O(n²)"),
        ("Heap Sort", "O(n log n)", "O(n log n)", "O(n log n)"),
        ("Counting Sort", "O(n + k)", "O(n + k)", "O(n + k)"),
        ("Python sorted() (Timsort)", "O(n)", "O(n log n)", "O(n log n)"),
    ]
    for metodo, mejor, promedio, peor in datos:
        print(f"{metodo:<25} {mejor:<15} {promedio:<15} {peor:<15}")
    print("=" * 70)
    print("\nNotas: k = rango de valores. Estable = mantiene orden de iguales. In-place = O(1) espacio extra.")


if __name__ == "__main__":
    print("=== Análisis de complejidad ===\n")
    analizar_complejidad()

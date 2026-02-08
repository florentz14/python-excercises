"""
05_Estructuras_de_Datos - Análisis de complejidad temporal
===========================================================
Tabla de mejor caso, promedio y peor caso por método.
Incluye todos los algoritmos de ordenamiento.
"""


def analizar_complejidad():
    """Imprime tabla de complejidades de todos los algoritmos."""
    print("\nComplejidad temporal de los métodos de ordenamiento:")
    print("=" * 90)
    print(f"{'Método':<28} {'Mejor':<14} {'Promedio':<14} {'Peor':<14} {'Espacio':<10} {'Estable'}")
    print("-" * 90)
    datos = [
        # Algoritmos O(n²) - Comparativos simples
        ("Bubble Sort",             "O(n)",       "O(n²)",      "O(n²)",      "O(1)",   "Sí"),
        ("Bubble Sort Optimizado",  "O(n)",       "O(n²)",      "O(n²)",      "O(1)",   "Sí"),
        ("Selection Sort",          "O(n²)",      "O(n²)",      "O(n²)",      "O(1)",   "No"),
        ("Insertion Sort",          "O(n)",       "O(n²)",      "O(n²)",      "O(1)",   "Sí"),
        ("Cocktail Sort",           "O(n)",       "O(n²)",      "O(n²)",      "O(1)",   "Sí"),
        ("Comb Sort",               "O(n log n)", "O(n²/2^p)",  "O(n²)",      "O(1)",   "No"),

        # Algoritmos O(n log n) - Comparativos eficientes
        ("Shell Sort (Knuth)",      "O(n log n)", "O(n^(4/3))", "O(n^(3/2))", "O(1)",   "No"),
        ("Merge Sort",              "O(n log n)", "O(n log n)", "O(n log n)", "O(n)",   "Sí"),
        ("Quick Sort",              "O(n log n)", "O(n log n)", "O(n²)",      "O(log n)", "No"),
        ("Heap Sort",               "O(n log n)", "O(n log n)", "O(n log n)", "O(1)",   "No"),
        ("Tim Sort",                "O(n)",       "O(n log n)", "O(n log n)", "O(n)",   "Sí"),

        # Algoritmos no comparativos
        ("Counting Sort",           "O(n + k)",   "O(n + k)",   "O(n + k)",   "O(k)",   "Sí"),
        ("Radix Sort",              "O(nk)",      "O(nk)",      "O(nk)",      "O(n+k)", "Sí"),
        ("Bucket Sort",             "O(n + k)",   "O(n + k)",   "O(n²)",      "O(n+k)", "Sí"),

        # Python built-in
        ("Python sorted() (Tim)",   "O(n)",       "O(n log n)", "O(n log n)", "O(n)",   "Sí"),
    ]
    for metodo, mejor, promedio, peor, espacio, estable in datos:
        print(f"{metodo:<28} {mejor:<14} {promedio:<14} {peor:<14} {espacio:<10} {estable}")
    print("=" * 90)

    print("""
Notas:
  n = número de elementos
  k = rango de valores (Counting/Radix) o número de cubetas (Bucket)
  p = número de incrementos (Comb Sort)
  Estable   = mantiene el orden relativo de elementos iguales
  In-place  = O(1) espacio extra (no cuenta la lista original)

Resumen:
  - Para listas pequeñas (<50):  Insertion Sort es excelente
  - Para uso general:            Tim Sort (Python sorted()) o Merge Sort
  - Para datos casi ordenados:   Tim Sort o Insertion Sort
  - Para enteros con rango acotado: Counting Sort o Radix Sort
  - Para datos uniformes:        Bucket Sort
  - Rápido in-place:             Quick Sort o Heap Sort
  - Shell Sort:                  Buen compromiso entre simplicidad y velocidad
""")


if __name__ == "__main__":
    print("=== Análisis de complejidad ===\n")
    analizar_complejidad()

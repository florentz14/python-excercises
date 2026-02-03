"""
05_Estructuras_de_Datos - Resumen y recomendaciones de ordenamiento
====================================================================
"""

print("=== Resumen y recomendaciones ===\n")
print("Recomendaciones de uso:")
print("=" * 70)
print("1. Listas pequeñas (< 50): Insertion Sort o Bubble Sort")
print("2. Listas medianas (50-1000): Quick Sort o Merge Sort")
print("3. Listas grandes (> 1000): Quick Sort, Merge Sort, Heap Sort o sorted()")
print("4. Rango de valores pequeño conocido: Counting Sort")
print("5. Necesitas estabilidad: Merge, Insertion, Bubble, Counting (evitar Quick, Heap)")
print("6. Poco espacio (in-place): Quick Sort, Heap Sort, Insertion Sort (evitar Merge)")
print("=" * 70)
print("\nMétodos implementados:")
print("  1. Bubble Sort - O(n²)")
print("  2. Selection Sort - O(n²)")
print("  3. Insertion Sort - O(n²) peor, O(n) mejor")
print("  4. Merge Sort - O(n log n), estable")
print("  5. Quick Sort - O(n log n) promedio")
print("  6. Heap Sort - O(n log n), in-place")
print("  7. Counting Sort - O(n + k)")
print("  8. Python sorted() - Timsort (híbrido)")

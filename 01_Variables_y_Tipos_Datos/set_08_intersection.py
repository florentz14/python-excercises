"""
Conjuntos (set) - Ejemplo 8: Intersección
=========================================
Tema: Conjuntos (01_Variables_y_Tipos_Datos)
Descripción: set_a & set_b devuelve elementos comunes a ambos.
"""

print("Example 8: Set intersection (common elements)")
print("-" * 40)
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "cherry", "date", "elderberry"}
print("Set A:", set_a)
print("Set B:", set_b)
intersection = set_a & set_b  # or set_a.intersection(set_b)
print("Intersection (set_a & set_b):", intersection)

"""
Conjuntos (set) - Ejemplo 17: Caso práctico - Elementos únicos
=============================================================
Tema: Conjuntos (01_Variables_y_Tipos_Datos)
Descripción: Usar set() sobre una lista para obtener valores únicos (ej. votos).
"""

print("Example 17: Practical example - Find unique elements")
print("-" * 40)
votes = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print("Votes:", votes)
unique_votes = set(votes)
print("Unique votes:", unique_votes)
print(f"Total votes: {len(votes)}")
print(f"Unique votes: {len(unique_votes)}")

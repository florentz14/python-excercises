"""
Conjuntos (set) - Ejemplo 11: Subconjunto y superconjunto
=========================================================
Tema: Conjuntos (01_Variables_y_Tipos_Datos)
Descripción: issubset(), issuperset(), isdisjoint() para comparar conjuntos.
"""

print("Example 11: Set comparison")
print("-" * 40)
parent_set = {1, 2, 3, 4, 5}
child_set = {2, 4}
print("Parent set:", parent_set)
print("Child set:", child_set)
print("Is child_set a subset of parent_set?", child_set.issubset(parent_set))
print("Is parent_set a superset of child_set?",
      parent_set.issuperset(child_set))
print("Are they disjoint?", child_set.isdisjoint(parent_set))

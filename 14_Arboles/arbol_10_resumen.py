"""
14_Arboles - Resumen de tipos de árboles
========================================
Comparación y aplicaciones.
"""

print("=== Resumen de tipos de árboles ===\n")
print("""
Tipos de Árboles:

1. ÁRBOL BINARIO:
   - Cada nodo tiene máximo 2 hijos
   - Operaciones: O(n) en el peor caso
   - Uso: Estructura básica

2. ÁRBOL BINARIO DE BÚSQUEDA (BST):
   - Árbol binario con propiedad de orden
   - Izquierda < Raíz < Derecha
   - Búsqueda: O(log n) promedio, O(n) peor caso
   - Uso: Búsqueda eficiente

3. ÁRBOL AVL:
   - BST auto-balanceado
   - Altura de subárboles difiere máximo en 1
   - Operaciones: O(log n) garantizado
   - Uso: Cuando se necesita garantía de rendimiento

4. ÁRBOL N-ARIO:
   - Cada nodo puede tener múltiples hijos
   - Uso: Representar jerarquías (archivos, organizaciones)

Recorridos:
- Preorden: Raíz -> Izquierda -> Derecha
- Inorden: Izquierda -> Raíz -> Derecha (ordena en BST)
- Postorden: Izquierda -> Derecha -> Raíz
- Por niveles (BFS): Nivel por nivel

Aplicaciones:
- Búsqueda y ordenamiento
- Expresiones matemáticas
- Estructuras de archivos
- Bases de datos (índices)
- Compresión (Huffman)
""")

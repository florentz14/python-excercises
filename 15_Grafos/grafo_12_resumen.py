"""
15_Grafos - Resumen de representaciones y algoritmos
=====================================================
"""

print("=== Resumen de grafos ===\n")
print("""
REPRESENTACIONES:

1. LISTA DE ADYACENCIA:
   - Ventajas: Poca memoria, fácil agregar nodos
   - Desventajas: Verificar arista más lento
   - Espacio: O(V + E). Uso: grafos dispersos

2. MATRIZ DE ADYACENCIA:
   - Ventajas: Verificar arista O(1), simple
   - Desventajas: Mucha memoria en grafos dispersos
   - Espacio: O(V²). Uso: grafos densos

ALGORITMOS:

1. BFS (Breadth First Search): O(V + E). Cola. Camino más corto (sin pesos).
2. DFS (Depth First Search): O(V + E). Pila. Ciclos, componentes conexas.
3. Dijkstra: camino más corto con pesos no negativos.
4. Ordenamiento topológico: O(V + E). Solo DAG. Scheduling, compilación.

APLICACIONES:
- Redes sociales, GPS, redes de computadoras
- Sistemas de recomendación, compiladores, scheduling
""")

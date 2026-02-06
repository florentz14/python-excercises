# Archivo: 48_05_resumen.py
# Descripción: Resumen de estructuras de datos avanzadas

if __name__ == "__main__":
    print("=== RESUMEN - Estructuras de Datos Avanzadas ===\n")
    print("""
Estructuras implementadas:

1. Trie (48_01):
   - Árbol de prefijos para strings
   - Búsqueda/inserción: O(m), m = longitud palabra
   - Uso: autocompletado, diccionarios, spell checkers

2. Segment Tree (48_02):
   - Consultas de rango (suma, mín, máx)
   - Consulta y actualización: O(log n)
   - Uso: rangos, RMQ

3. Fenwick Tree (48_03):
   - Sumas de prefijos
   - Consulta y actualización: O(log n)
   - Uso: sumas acumulativas, inversiones

4. Union-Find mejorado (48_04):
   - Path compression + union by rank
   - Casi O(1) en la práctica
   - Uso: ciclos, Kruskal, componentes conexas

Complejidades:
- Trie: O(m) búsqueda/inserción
- Segment Tree: O(log n) consulta/actualización, O(n) espacio
- Fenwick Tree: O(log n) consulta/actualización, O(n) espacio
- Union-Find: O(α(n)) ≈ constante
""")

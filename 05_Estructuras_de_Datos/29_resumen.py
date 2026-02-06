# Archivo: 47_07_resumen.py
# Descripción: Resumen de algoritmos de backtracking

if __name__ == "__main__":
    print("=== RESUMEN - Algoritmos de Backtracking ===\n")
    print("""
Algoritmos implementados:

1. N-Reinas (47_01):
   - N reinas en tablero NxN sin que se ataquen
   - Complejidad: O(N!)

2. Solucionador de Sudoku (47_02):
   - Sudoku 9x9 con backtracking
   - Complejidad: O(9^m), m = celdas vacías

3. Resolución de Laberintos (47_03):
   - Camino desde inicio a destino
   - Complejidad: O(4^(n*m)) peor caso

4. Permutaciones (47_04):
   - Todas las permutaciones de n elementos
   - Complejidad: O(n! * n)

5. Combinaciones (47_05):
   - Combinaciones de k de n elementos
   - Complejidad: O(C(n,k) * k)

6. Subset Sum (47_06):
   - Subconjuntos que sumen un objetivo
   - Complejidad: O(2^n), NP-completo

Características del Backtracking:
- Búsqueda sistemática
- Construye soluciones incrementalmente
- Abandona soluciones parciales inviables
- Complejidad típicamente exponencial

Cuándo usar:
- Problemas con restricciones
- Búsqueda exhaustiva
- Puzzles y juegos
- Optimización discreta
""")

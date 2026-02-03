# Archivo: 44_07_resumen.py
# Descripción: Resumen de algoritmos avanzados de strings

if __name__ == "__main__":
    print("=== RESUMEN - Algoritmos Avanzados de Strings ===\n")
    print("""
Algoritmos implementados:

1. Rabin-Karp (44_01):
   - Búsqueda de patrón con rolling hash
   - Complejidad: O(n + m) promedio
   - Útil para múltiples patrones

2. Z-Algorithm (44_02):
   - Z-array y búsqueda de patrones
   - Complejidad: O(n + m)

3. Longest Common Substring (44_03):
   - Subcadena común más larga entre dos strings
   - Complejidad: O(m * n)

4. Edit Distance - Levenshtein (44_04):
   - Mínimo de operaciones (insertar, eliminar, sustituir)
   - Complejidad: O(m * n)

5. Longest Palindromic Substring (44_05):
   - Palíndromo más largo (expansión desde centro)
   - Complejidad: O(n²)

6. Anagramas y Permutaciones (44_06):
   - Detección de anagramas, agrupación, permutaciones

Aplicaciones:
- Búsqueda de texto (grep, editores)
- Corrección ortográfica
- Comparación de secuencias
- Análisis de texto y NLP
""")

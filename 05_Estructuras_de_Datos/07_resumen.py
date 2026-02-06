# Archivo: 42_07_resumen.py
# Descripción: Resumen de algoritmos greedy

if __name__ == "__main__":
    print("=== RESUMEN - Algoritmos Greedy ===\n")
    print("""
Algoritmos Greedy implementados:

1. Mochila Fraccionaria (42_01):
   - Estrategia: Tomar items con mayor valor/peso primero
   - Complejidad: O(n log n)
   - Siempre da solución óptima

2. Selección de Actividades (42_02):
   - Estrategia: Seleccionar actividades que terminan primero
   - Complejidad: O(n log n)
   - Siempre da solución óptima

3. Algoritmo de Kruskal - MST (42_03):
   - Estrategia: Agregar aristas más ligeras que no formen ciclos
   - Complejidad: O(E log E)
   - Siempre da solución óptima

4. Codificación de Huffman (42_04):
   - Estrategia: Combinar nodos con menor frecuencia
   - Complejidad: O(n log n)
   - Siempre da solución óptima

5. Cambio de Monedas (42_05):
   - Estrategia: Usar monedas más grandes primero
   - Complejidad: O(n)
   - Solo funciona para sistemas canónicos

6. Interval Scheduling con Pesos (42_06):
   - Versión simplificada (completa requiere DP)
   - Complejidad: O(n²)

Características de Algoritmos Greedy:
- Hacen la elección localmente óptima en cada paso
- No reconsideran decisiones previas
- Eficientes pero no siempre óptimos
- Funcionan bien para problemas con subestructura óptima
""")

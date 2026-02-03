"""
05_Estructuras_de_Datos - Resumen de algoritmos de búsqueda
============================================================
"""

print("=== Resumen: Algoritmos de busqueda ===\n")
print("""
1. Busqueda Lineal O(n):
   - Listas no ordenadas
   - Simple. Util para listas pequenas

2. Busqueda Binaria O(log n):
   - REQUIERE lista ordenada
   - Muy eficiente para listas grandes
   - Variantes: primera/ultima ocurrencia

3. Busqueda en strings:
   - Fuerza bruta: O(n*m)
   - KMP: O(n+m), mejor para patrones largos

4. Utilidades:
   - Posicion de insercion (mantener orden)
   - Conteo de ocurrencias en lista ordenada

Recomendaciones:
- Lineal: listas pequenas (< 100) o no ordenadas
- Binaria: listas grandes y ordenadas
- KMP: busquedas repetidas de patron en texto largo
""")

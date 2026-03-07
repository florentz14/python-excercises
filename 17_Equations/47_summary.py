# Archivo: 49_06_resumen.py
# Descripción: Resumen de métodos numéricos

if __name__ == "__main__":
    print("=== RESUMEN - Métodos Numéricos ===\n")
    print("""
Métodos implementados:

1. Newton-Raphson (49_01):
   - Raíces de ecuaciones no lineales
   - Convergencia cuadrática, requiere derivada
   - O(k) iteraciones

2. Interpolación de Lagrange (49_02):
   - Polinomio que pasa por puntos dados
   - O(n²) para n puntos

3. Interpolación de Newton (49_03):
   - Diferencias divididas
   - O(n²)

4. Regresión Lineal (49_04):
   - Recta y = mx + b, mínimos cuadrados, R²
   - O(n)

5. Regresión Polinomial (49_05):
   - Polinomio de grado k, mínimos cuadrados
   - O(n³) (sistema normal)
   - Requiere NumPy

Aplicaciones:
- Raíces de ecuaciones (ingeniería)
- Interpolación y extrapolación
- Ajuste de datos y ML básico
""")

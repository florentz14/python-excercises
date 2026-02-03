# 52_08_resumen.py - Resumen del módulo de ecuaciones diferenciales

print("=== Resumen: Ecuaciones Diferenciales ===\n")
print("""
1. Método de Euler (52_01):
   - dy/dt = f(t, y), paso fijo
   - Simple, menos preciso

2. Runge-Kutta orden 4 (52_02):
   - Más preciso que Euler
   - Comparación de errores

3. scipy.solve_ivp (52_03):
   - Método RK45 con adaptación de paso
   - Uso estándar para EDOs en Python

4. Modelo de crecimiento (52_04):
   - Malthus: dy/dt = r*y (exponencial)

5. Modelo logístico (52_05):
   - dy/dt = r*y*(1 - y/K), capacidad de carga K

6. Sistema de EDOs (52_06):
   - Predador-presa (Lotka-Volterra)
   - Plano de fase

7. EDO de segundo orden (52_07):
   - Reducción a sistema de primer orden
   - Oscilador armónico

Todos resuelven dy/dt = f(t, y). Para orden superior se convierte en sistema.
Requisitos: NumPy, SciPy, Matplotlib.
""")

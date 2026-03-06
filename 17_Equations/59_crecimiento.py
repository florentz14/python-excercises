# 52_04_crecimiento.py - Modelo de crecimiento poblacional (Malthus)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

print("=== 4. Modelo de Crecimiento Poblacional ===\n")
print("dy/dt = r * y (crecimiento exponencial)\n")


def crecimiento_poblacional(t, y, r=0.1):
    """Modelo de Malthus: crecimiento exponencial"""
    return r * y


r_tasa = 0.1
poblacion_inicial = 1000

sol = solve_ivp(
    lambda t, y: crecimiento_poblacional(t, y, r_tasa),
    [0, 50],
    [poblacion_inicial],
    t_eval=np.linspace(0, 50, 100)
)

print(f"Población inicial: {poblacion_inicial}")
print(f"Población en t=50: {sol.y[0][-1]:.2f}")

plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], 'g-', linewidth=2)
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Modelo de Crecimiento Exponencial (Malthus)')
plt.grid(True, alpha=0.3)
plt.show()

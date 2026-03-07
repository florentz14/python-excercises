# 52_05_logistico.py - Modelo logístico de crecimiento

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

print("=== 5. Modelo Logístico ===\n")
print("dy/dt = r * y * (1 - y/K), K = capacidad de carga\n")


def modelo_logistico(t, y, r=0.1, K=5000):
    return r * y * (1 - y / K)


sol = solve_ivp(
    lambda t, y: modelo_logistico(t, y, r=0.15, K=5000),
    [0, 100],
    [100],
    t_eval=np.linspace(0, 100, 200)
)

print(f"Capacidad de carga (K): 5000")
print(f"Población inicial: 100")
print(f"Población final: {sol.y[0][-1]:.2f}")

plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], 'b-', linewidth=2, label='Población')
plt.axhline(y=5000, color='r', linestyle='--', label='Capacidad de Carga (K)')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Modelo Logístico de Crecimiento Poblacional')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

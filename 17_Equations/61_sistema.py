# 52_06_sistema.py - Sistema de EDOs: modelo predador-presa (Lotka-Volterra)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

print("=== 6. Sistema de Ecuaciones Diferenciales ===\n")
print("Modelo Predador-Presa (Lotka-Volterra)\n")


def sistema_predador_presa(t, y, a=1.0, b=0.1, c=1.5, d=0.075):
    """dx/dt = a*x - b*x*y (presa), dy/dt = -c*y + d*x*y (predador)"""
    x, y_pred = y
    dxdt = a * x - b * x * y_pred
    dydt = -c * y_pred + d * x * y_pred
    return [dxdt, dydt]


condiciones_iniciales = [10, 5]  # 10 presas, 5 predadores
t_sistema = np.linspace(0, 50, 1000)

sol = solve_ivp(
    lambda t, y: sistema_predador_presa(t, y),
    [0, 50],
    condiciones_iniciales,
    t_eval=t_sistema
)

print(f"Condiciones iniciales: {condiciones_iniciales[0]} presas, {condiciones_iniciales[1]} predadores")

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(sol.t, sol.y[0], 'g-', label='Presas', linewidth=2)
plt.plot(sol.t, sol.y[1], 'r-', label='Predadores', linewidth=2)
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Modelo Predador-Presa (Temporal)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(sol.y[0], sol.y[1], 'b-', linewidth=1.5)
plt.plot(sol.y[0][0], sol.y[1][0], 'go', markersize=10, label='Inicio')
plt.xlabel('Presas')
plt.ylabel('Predadores')
plt.title('Plano de Fase')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

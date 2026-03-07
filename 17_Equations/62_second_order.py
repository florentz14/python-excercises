# 52_07_segundo_orden.py - EDO de segundo orden: oscilador armónico

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

print("=== 7. Ecuación Diferencial de Segundo Orden ===\n")
print("Oscilador Armónico: d2y/dt2 + omega^2*y = 0\n")


def oscilador_armonico(t, y, omega=1.0):
    """Sistema: y1=y, y2=dy/dt; dy1/dt=y2, dy2/dt=-omega^2*y1"""
    y1, y2 = y
    return [y2, -omega**2 * y1]


omega = 2.0
sol = solve_ivp(
    lambda t, y: oscilador_armonico(t, y, omega),
    [0, 10],
    [1, 0],  # y(0)=1, y'(0)=0
    t_eval=np.linspace(0, 10, 200)
)

y_exacta = np.cos(omega * sol.t)

print(f"Frecuencia angular (omega): {omega}")
print(f"Valor en t=10 (numérico): {sol.y[0][-1]:.6f}")
print(f"Valor en t=10 (exacto): {y_exacta[-1]:.6f}")

plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], 'b-', label='Solución Numérica', linewidth=2)
plt.plot(sol.t, y_exacta, 'r--', label='Solución Exacta: cos(omega*t)', linewidth=2)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Oscilador Armónico: d2y/dt2 + omega^2*y = 0')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

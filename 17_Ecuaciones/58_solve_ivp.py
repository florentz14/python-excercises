# 52_03_solve_ivp.py - Resolución con scipy.integrate.solve_ivp

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

print("=== 3. Usando scipy.integrate.solve_ivp ===\n")


def ejemplo_derivada(t, y):
    """dy/dt = t * y, y(0) = 1. Solución exacta: y = e^(t^2/2)"""
    return t * y


solucion = solve_ivp(ejemplo_derivada, [0, 2], [1],
                     t_eval=np.linspace(0, 2, 100),
                     method='RK45')

print("Ejemplo: dy/dt = t*y, y(0) = 1")
print(f"Valor en t=2: {solucion.y[0][-1]:.6f}")
print(f"Solución exacta: {np.exp(2**2/2):.6f}")

plt.figure(figsize=(10, 6))
plt.plot(solucion.t, solucion.y[0], 'b-', label='Solución Numérica', linewidth=2)
plt.plot(solucion.t, np.exp(solucion.t**2 / 2), 'r--',
         label='Solución Exacta: y = e^(t^2/2)', linewidth=2)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('scipy.solve_ivp: dy/dt = t*y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

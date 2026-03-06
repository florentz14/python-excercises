# 52_01_euler.py - Método de Euler para EDOs
# Resolución de dy/dt = f(t, y) con método de Euler

import numpy as np
import matplotlib.pyplot as plt

print("=== 1. Método de Euler ===\n")


def metodo_euler(f, y0, t0, tf, n_pasos):
    """
    Resuelve una ecuación diferencial dy/dt = f(t, y) usando el método de Euler.
    Retorna: (t_array, y_array)
    """
    h = (tf - t0) / n_pasos
    t = np.linspace(t0, tf, n_pasos + 1)
    y = np.zeros(n_pasos + 1)
    y[0] = y0

    for i in range(n_pasos):
        y[i + 1] = y[i] + h * f(t[i], y[i])

    return t, y


# Ejemplo: dy/dt = -2y, y(0) = 1. Solución analítica: y(t) = e^(-2t)
def ejemplo_derivada(t, y):
    return -2 * y


t_euler, y_euler = metodo_euler(ejemplo_derivada, y0=1, t0=0, tf=2, n_pasos=50)
y_exacta = np.exp(-2 * t_euler)

print("Ejemplo: dy/dt = -2y, y(0) = 1")
print(f"Valor en t=2 (Euler): {y_euler[-1]:.6f}")
print(f"Valor en t=2 (Exacta): {y_exacta[-1]:.6f}")
print(f"Error: {abs(y_euler[-1] - y_exacta[-1]):.6f}")

plt.figure(figsize=(10, 6))
plt.plot(t_euler, y_euler, 'b-', label='Método de Euler', linewidth=2)
plt.plot(t_euler, y_exacta, 'r--', label='Solución Exacta', linewidth=2)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Método de Euler: dy/dt = -2y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

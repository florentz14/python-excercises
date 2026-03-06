# 52_02_runge_kutta.py - Método de Runge-Kutta orden 4 y comparación con Euler

import numpy as np
import matplotlib.pyplot as plt

print("=== 2. Método de Runge-Kutta (Orden 4) ===\n")


def metodo_euler(f, y0, t0, tf, n_pasos):
    h = (tf - t0) / n_pasos
    t = np.linspace(t0, tf, n_pasos + 1)
    y = np.zeros(n_pasos + 1)
    y[0] = y0
    for i in range(n_pasos):
        y[i + 1] = y[i] + h * f(t[i], y[i])
    return t, y


def runge_kutta_4(f, y0, t0, tf, n_pasos):
    """Runge-Kutta de orden 4. Más preciso que Euler."""
    h = (tf - t0) / n_pasos
    t = np.linspace(t0, tf, n_pasos + 1)
    y = np.zeros(n_pasos + 1)
    y[0] = y0
    for i in range(n_pasos):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + h/2, y[i] + k1/2)
        k3 = h * f(t[i] + h/2, y[i] + k2/2)
        k4 = h * f(t[i] + h, y[i] + k3)
        y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    return t, y


def ejemplo_derivada(t, y):
    return -2 * y


t_euler, y_euler = metodo_euler(ejemplo_derivada, y0=1, t0=0, tf=2, n_pasos=50)
t_rk, y_rk = runge_kutta_4(ejemplo_derivada, y0=1, t0=0, tf=2, n_pasos=50)
y_exacta = np.exp(-2 * t_euler)

print("Comparación Euler vs Runge-Kutta (dy/dt = -2y):")
print(f"Euler - Error en t=2: {abs(y_euler[-1] - y_exacta[-1]):.6f}")
print(f"RK4   - Error en t=2: {abs(y_rk[-1] - y_exacta[-1]):.6f}")

plt.figure(figsize=(10, 6))
plt.plot(t_euler, y_euler, 'b-', label='Método de Euler', linewidth=2, alpha=0.7)
plt.plot(t_rk, y_rk, 'g-', label='Runge-Kutta 4', linewidth=2, alpha=0.7)
plt.plot(t_euler, y_exacta, 'r--', label='Solución Exacta', linewidth=2)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Comparación de Métodos: dy/dt = -2y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

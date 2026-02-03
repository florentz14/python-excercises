# Archivo: 31_04_graficar.py
# Descripción: Graficar función y área bajo la curva (integral)

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


def graficar_integral(funcion, a, b, titulo="Integral Definida"):
    """
    Grafica la función y el área bajo la curva (integral).
    """
    try:
        x = np.linspace(a - 1, b + 1, 1000)
        y = funcion(x)

        resultado, error = spi.quad(funcion, a, b)

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2, label='f(x)')

        x_area = np.linspace(a, b, 1000)
        y_area = funcion(x_area)
        plt.fill_between(x_area, y_area, alpha=0.3, color='green',
                         label=f'Area = {resultado:.4f}')

        plt.axvline(x=a, color='r', linestyle='--', linewidth=1, label=f'a = {a}')
        plt.axvline(x=b, color='r', linestyle='--', linewidth=1, label=f'b = {b}')
        plt.axhline(y=0, color='k', linewidth=0.5)

        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.title(f'{titulo}\nIntegral f(x)dx de {a} a {b} = {resultado:.4f}',
                  fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()

        return resultado, error

    except Exception as e:
        print(f"Error al graficar: {e}")
        return None, None


if __name__ == "__main__":
    from integracion_util import f_original

    print("=== Versión 4: Con Visualización Gráfica ===\n")
    print("Graficando integral de la función original:")
    graficar_integral(f_original, -4, -3, "f(x) = -x^2 - 2x + 8")

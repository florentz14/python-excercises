# Archivo: 27_04_graficar.py
# Descripción: Graficar ecuación cuadrática y marcar raíces/vértice

import numpy as np
import matplotlib.pyplot as plt

from resolver_cuadratica import ecuacion_cuadratica_completa


def graficar_ecuacion_cuadratica(a, b, c, x_min=-10, x_max=10, mostrar_raices=True):
    """
    Grafica una ecuación cuadrática y marca las raíces si existen.
    """
    try:
        x = np.linspace(x_min, x_max, 1000)
        y = a*x**2 + b*x + c

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2, label=f'{a}x² + {b}x + {c} = 0')

        plt.axhline(y=0, color='k', linewidth=0.5, linestyle='--')
        plt.axvline(x=0, color='k', linewidth=0.5, linestyle='--')

        if mostrar_raices:
            soluciones = ecuacion_cuadratica_completa(a, b, c, solo_reales=True)
            if soluciones:
                for sol in soluciones:
                    if isinstance(sol, (int, float)) and x_min <= sol <= x_max:
                        plt.plot(sol, 0, 'ro', markersize=10, label=f'Raíz: x = {sol:.2f}')

        x_vertice = -b / (2*a)
        y_vertice = a*x_vertice**2 + b*x_vertice + c
        if x_min <= x_vertice <= x_max:
            plt.plot(x_vertice, y_vertice, 'go', markersize=8,
                     label=f'Vértice: ({x_vertice:.2f}, {y_vertice:.2f})')

        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.title(f'Gráfica de {a}x² + {b}x + {c} = 0', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error al graficar: {e}")


if __name__ == "__main__":
    print("=== Versión 4: Graficar Ecuación Cuadrática ===\n")
    print("Graficando x² + 8x + 12 = 0")
    graficar_ecuacion_cuadratica(1, 8, 12)

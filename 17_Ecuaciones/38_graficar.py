# Archivo: 35_05_graficar.py
# Descripción: Visualización gráfica de la suma de Riemann

import numpy as np
import matplotlib.pyplot as plt

from riemann_util import f, a, b, suma_riemann_vectorizada


def graficar_suma_riemann(funcion, a_lim, b_lim, n_sub=20, metodo='punto_medio'):
    """
    Grafica la suma de Riemann.
    """
    try:
        dx = (b_lim - a_lim) / n_sub
        x_continuo = np.linspace(a_lim, b_lim, 1000)
        y_continuo = funcion(x_continuo)

        if metodo == 'izquierda':
            x_barras = np.linspace(a_lim, b_lim - dx, n_sub)
        elif metodo == 'derecha':
            x_barras = np.linspace(a_lim + dx, b_lim, n_sub)
        else:
            x_barras = np.linspace(a_lim + dx/2, b_lim - dx/2, n_sub)

        y_barras = funcion(x_barras)

        plt.figure(figsize=(12, 6))
        plt.plot(x_continuo, y_continuo, 'b-', linewidth=2, label='f(x)')

        for i in range(n_sub):
            x_etiqueta = x_barras[i]
            plt.bar(x_etiqueta, y_barras[i], width=dx, alpha=0.3,
                   color='green', edgecolor='black', align='center')

        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=a_lim, color='r', linestyle='--', linewidth=1, label=f'a = {a_lim}')
        plt.axvline(x=b_lim, color='r', linestyle='--', linewidth=1, label=f'b = {b_lim}')

        aproximacion = suma_riemann_vectorizada(funcion, a_lim, b_lim, n_sub, metodo)
        titulo_metodo = metodo.replace("_", " ").title()
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.title(f'Suma de Riemann ({titulo_metodo}) - n={n_sub}\nAproximación: {aproximacion:.6f}',
                  fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()

        return aproximacion

    except Exception as e:
        print(f"Error al graficar: {e}")
        return None


if __name__ == "__main__":
    print("=== Versión 5: Visualización Gráfica ===\n")
    print("Graficando suma de Riemann (punto medio, n=20):")
    graficar_suma_riemann(f, a, b, n_sub=20, metodo='punto_medio')

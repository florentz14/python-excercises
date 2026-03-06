# Programa para graficar diferentes funciones matemáticas
import matplotlib.pyplot as plt  # Para crear gráficos
import numpy as np  # Para trabajar con arreglos numéricos

# Crear una figura con múltiples subgráficos
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Gráficas de Diferentes Funciones",
             fontsize=16, fontweight='bold')

# Función 1: Parábola (Función Cuadrática)
x1 = np.linspace(-5, 5, 100)  # Valores de X desde -5 hasta 5
y1 = x1**2  # Elevar al cuadrado: f(x) = x²
axes[0, 0].plot(x1, y1, 'b-', linewidth=2)  # Dibujar en azul
axes[0, 0].set_title("Función Cuadrática: f(x) = x²")
axes[0, 0].set_xlabel("X")
axes[0, 0].set_ylabel("Y")
axes[0, 0].grid(True, alpha=0.3)

# Función 2: Función Exponencial
x2 = np.linspace(-3, 3, 100)  # Valores de X desde -3 hasta 3
y2 = np.exp(x2)  # e elevado a x: f(x) = e^x
axes[0, 1].plot(x2, y2, 'r-', linewidth=2)  # Dibujar en rojo
axes[0, 1].set_title("Función Exponencial: f(x) = e^x")
axes[0, 1].set_xlabel("X")
axes[0, 1].set_ylabel("Y")
axes[0, 1].grid(True, alpha=0.3)

# Función 3: Función Logarítmica
x3 = np.linspace(0.1, 5, 100)  # Valores de X desde 0.1 hasta 5
y3 = np.log(x3)  # Logaritmo natural: f(x) = ln(x)
axes[1, 0].plot(x3, y3, 'g-', linewidth=2)  # Dibujar en verde
axes[1, 0].set_title("Función Logarítmica: f(x) = ln(x)")
axes[1, 0].set_xlabel("X")
axes[1, 0].set_ylabel("Y")
axes[1, 0].grid(True, alpha=0.3)

# Función 4: Función Cúbica
x4 = np.linspace(-3, 3, 100)  # Valores de X desde -3 hasta 3
y4 = x4**3  # Elevar al cubo: f(x) = x³
axes[1, 1].plot(x4, y4, 'm-', linewidth=2)  # Dibujar en magenta
axes[1, 1].set_title("Función Cúbica: f(x) = x³")
axes[1, 1].set_xlabel("X")
axes[1, 1].set_ylabel("Y")
axes[1, 1].grid(True, alpha=0.3)

# Ajustar el espaciado entre los subgráficos
plt.tight_layout()

# Mostrar la gráfica en la pantalla
plt.show()

# Importar las librerías necesarias
import matplotlib.pyplot as plt  # Para crear gráficos
import numpy as np  # Para trabajar con arreglos numéricos

# Crear valores en el eje X desde 0 hasta 10 con 100 puntos o divisiones
x = np.linspace(0, 10, 100)
# Calcular el seno de cada valor en X
y = np.sin(x)
# Dibujar la gráfica de la onda senoidal
plt.plot(x, y)
# Establecer el título de la gráfica
plt.title("Sine Wave")
# Etiqueta para el eje X
plt.xlabel("X-axis")
# Etiqueta para el eje Y
plt.ylabel("Y-axis")
# Mostrar la grilla (cuadrícula)
plt.grid(True)
# Mostrar la gráfica en la pantalla
plt.show()

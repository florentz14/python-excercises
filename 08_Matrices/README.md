# 08_Matrices

Ejercicios de **vectores** y **matrices**: primero con **Python básico** (listas) y luego **NumPy paso a paso**.

---

## Ruta: Python básico → NumPy paso a paso

| Orden | Archivo | Contenido |
|-------|---------|-----------|
| **Python básico** | `vector_01` … `vector_06` | Vectores con listas |
| | `matrix_01` … `matrix_06` | Matrices con lista de listas |
| **NumPy paso 1** | `numpy_01_instalar_importar.py` | `pip install numpy`, `import numpy as np` |
| **NumPy paso 2** | `numpy_02_crear_array.py` | `np.array(lista)`, `.shape`, `.dtype`, `zeros`, `ones` |
| **NumPy paso 3** | `numpy_03_vectores.py` | `v + w`, `k * v`, `np.dot(v,w)`, `np.linalg.norm(v)` |
| **NumPy paso 4** | `numpy_04_matrices.py` | `A + B`, `k * A`, `A.T` (transpuesta) |
| **NumPy paso 5** | `numpy_05_multiplicacion.py` | `A @ B`, matriz × vector |
| **NumPy paso 6** | `numpy_06_resumen.py` | Tabla Python vs NumPy |

Recomendación: hacer primero los ejercicios de vectores y matrices con listas, luego seguir `numpy_01` → `numpy_06` en orden.

---

## Python básico (listas)

### Vectores

Los vectores se representan como **listas** de números.

| Archivo | Contenido |
|---------|-----------|
| `vector_01_crear_mostrar.py` | Crear y mostrar un vector |
| `vector_02_suma.py` | Suma de vectores |
| `vector_03_producto_escalar.py` | Vector × escalar |
| `vector_04_producto_punto.py` | Producto punto (escalar) |
| `vector_05_magnitud.py` | Magnitud (norma) de un vector |
| `vector_06_resta.py` | Resta de vectores |

### Matrices

Las matrices se representan como **lista de listas** (cada sublista es una fila).

| Archivo | Contenido |
|---------|-----------|
| `matrix_01_crear_mostrar.py` | Crear y mostrar una matriz |
| `matrix_02_suma.py` | Suma de matrices |
| `matrix_03_producto_escalar.py` | Matriz × escalar |
| `matrix_04_transpuesta.py` | Transpuesta A^T |
| `matrix_05_multiplicar.py` | Multiplicación A * B |
| `matrix_06_matriz_por_vector.py` | Matriz × vector (columna) |

---

## NumPy (paso a paso)

| Archivo | Contenido |
|---------|-----------|
| `numpy_01_instalar_importar.py` | Instalar e importar NumPy |
| `numpy_02_crear_array.py` | Crear arrays desde listas, `.shape`, `zeros`, `ones` |
| `numpy_03_vectores.py` | Operaciones con vectores (suma, escalar, producto punto, norma) |
| `numpy_04_matrices.py` | Operaciones con matrices (suma, escalar, transpuesta) |
| `numpy_05_multiplicacion.py` | Multiplicación A @ B y matriz × vector |
| `numpy_06_resumen.py` | Resumen Python básico vs NumPy |
| `numpy_07_linalg.py` | Álgebra lineal: dot, norm, inverse (con cuidado) |
| `numpy_08_broadcasting.py` | Broadcasting (arrays de distintas formas) |

---

## Ejecutar

Desde la raíz del proyecto:

```bash
# Instalar dependencias (una vez)
pip install -r requirements.txt

# Python básico (no requiere NumPy)
python 08_Matrices/vector_01_crear_mostrar.py
python 08_Matrices/matrix_01_crear_mostrar.py

# NumPy
python 08_Matrices/numpy_01_instalar_importar.py
python 08_Matrices/numpy_03_vectores.py
```

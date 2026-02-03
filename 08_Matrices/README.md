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
| `matrix_07_crear_acceso_modificar.py` | Crear, acceder, modificar elemento, dimensiones |
| `matrix_08_ceros_identidad.py` | Matriz de ceros y matriz identidad |
| `matrix_09_transpuesta_suma_escalar.py` | Transpuesta, suma A+B, producto por escalar |
| `matrix_10_fila_columna_suma_maxmin.py` | Obtener fila/columna, suma total, máximo y mínimo |
| `matrix_11_formato_tipos_cuadrado.py` | Imprimir en grid, tipos mixtos, verificar si es cuadrada |
| `matrix_12_rotar_diagonal_recorrido.py` | Rotar 90°, diagonal principal, recorrido por índices |
| `matrix_13_comprehension_practico.py` | Crear por comprensión, ejemplo notas de estudiantes |
| `matrix_14_suma_resta_escalar.py` | Suma A+B, resta A-B, producto por escalar k*A |
| `matrix_15_multiplicacion_hadamard.py` | Multiplicación C×D y producto Hadamard (elemento a elemento) |
| `matrix_16_transpuesta_division_negacion.py` | Transpuesta, división por escalar, negación -A |
| `matrix_17_identidad_trace_determinante.py` | Identidad×matriz, traza, determinante 2×2 |
| `matrix_18_sumas_filas_columnas.py` | Suma total, sumas por fila y por columna |
| `matrix_19_division_elemental_potencia.py` | División elemento a elemento, matriz al cuadrado |
| `matrix_20_ejemplos_practicos.py` | Brillo de imagen (píxeles), ventas Q1+Q2 y crecimiento |

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

## Rango de matriz (34_xx)

Cálculo del **rango** de una matriz con NumPy (`np.linalg.matrix_rank` y análisis).

- **rango_matriz_util.py** — Matriz de ejemplo `A` (3×4) y función `calcular_rango_matriz`.

| Archivo | Contenido |
|---------|-----------|
| `34_01_original.py` | Versión original: imprimir matriz y rango |
| `34_02_optimizada.py` | Rango con información (full rank / rank deficient) |
| `34_03_analisis_completo.py` | Análisis: espacios, determinante si es cuadrada |
| `34_04_comparar_metodos.py` | Comparar matrix_rank, SVD, QR |
| `34_05_ejemplos_tipos.py` | Ejemplos: identidad, rango completo/reducido, cero, rectangulares |
| `34_06_propiedades.py` | Propiedades: rank(A)=rank(A^T), rank(AB), etc. |
| `34_07_interactiva.py` | Menú interactivo (ejemplo o matriz personalizada) |
| `34_08_resumen.py` | Resumen del análisis y conceptos |

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

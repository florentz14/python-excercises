# 17_Ecuaciones

Sistemas lineales (NumPy), ecuaciones cuadráticas (math/cmath) e integración numérica (SciPy).

## Estructura

### Módulos compartidos

- **datos_sistema.py** — Datos compartidos para sistemas lineales (matrices A, b y variantes).
- **resolver_mejorado.py** — Función `resolver_sistema_mejorado` para sistemas lineales.
- **resolver_cuadratica.py** — Función `ecuacion_cuadratica_completa` para ecuaciones cuadráticas.
- **integracion_util.py** — `f_original` y `integrar_funcion` para integración numérica.
- **riemann_util.py** — `f`, `suma_riemann_vectorizada`, `regla_trapecio`, `regla_simpson` y parámetros a, b, n para sumas de Riemann.

### Sistemas lineales (25_xx)

| Archivo | Descripción |
|---------|-------------|
| 25_01_original.py | Versión original: determinante + `np.linalg.solve` |
| 25_02_mejorado.py | Versión optimizada con validación y verificación |
| 25_03_multiples_sistemas.py | Múltiples sistemas Ax = b (columnas de B) |
| 25_04_fracciones.py | Solución en decimales y fracciones |
| 25_05_analisis_completo.py | Análisis: determinante, rango, condición, verificación |
| 25_06_sistemas_ejemplos.py | Sistemas original (A,b) y comentado (B,d) |
| 25_07_comparar_metodos.py | Comparación: solve, inversa, lstsq |
| 25_08_resumen.py | Resumen del módulo de sistemas lineales |

### Ecuaciones cuadráticas (27_xx)

| Archivo | Descripción |
|---------|-------------|
| 27_01_original.py | Versión original (solo soluciones reales) |
| 27_02_optimizada.py | Con números complejos |
| 27_03_analisis_completo.py | Análisis: discriminante, vértice, concavidad |
| 27_04_graficar.py | Graficar parábola y marcar raíces/vértice |
| 27_05_multiples_ecuaciones.py | Resolver varias ecuaciones |
| 27_06_interactiva.py | Entrada interactiva (input) |
| 27_07_verificacion.py | Verificar que las soluciones cumplan la ecuación |
| 27_08_resumen.py | Resumen del módulo cuadráticas |

### Integración numérica (31_xx)

| Archivo | Descripción |
|---------|-------------|
| 31_01_original.py | Versión original (quad, una función) |
| 31_02_optimizada.py | Integración con detalles y error estimado |
| 31_03_multiples_funciones.py | Integrar varias funciones en [a,b] |
| 31_04_graficar.py | Graficar función y área bajo la curva |
| 31_05_comparar_metodos.py | Comparar quad, fixed_quad, romberg, simpson, trapezoid |
| 31_06_impropias.py | Integrales impropias (límites infinitos) |
| 31_07_multiples.py | Integrales dobles (dblquad) |
| 31_08_interactiva.py | Calculadora interactiva de integrales |
| 31_09_verificacion.py | Verificación analítica vs numérica |
| 31_10_resumen.py | Resumen del módulo integración |

### Sistema de ecuaciones ejemplo específico (33_xx)

Sistema: x + y + z = 2,  2x + z = 1,  x + 2y = 5.

- **datos_ejemplo_33.py** — A, b para este sistema.

| Archivo | Descripción |
|---------|-------------|
| 33_01_original.py | Versión original (determinante + solve) |
| 33_02_mejorado.py | Resolver con `resolver_mejorado` |
| 33_03_analisis_completo.py | Análisis: determinante, rango, condición, fracciones |
| 33_04_paso_a_paso.py | Matriz aumentada y solución paso a paso |
| 33_05_verificacion_manual.py | Verificación ecuación por ecuación |
| 33_06_comparar_metodos.py | solve, inversa, lstsq |
| 33_07_resumen.py | Resumen del análisis |

### Métodos numéricos (49_xx)

| Archivo | Descripción |
|---------|-------------|
| 49_01_newton_raphson.py | Newton-Raphson para raíces de f(x)=0 |
| 49_02_lagrange.py | Interpolación de Lagrange |
| 49_03_newton_interpolacion.py | Interpolación de Newton (diferencias divididas) |
| 49_04_regresion_lineal.py | Regresión lineal (mínimos cuadrados, R²) |
| 49_05_regresion_polinomial.py | Regresión polinomial (NumPy) |
| 49_06_resumen.py | Resumen de métodos numéricos |

### Ecuaciones diferenciales (52_xx)

| Archivo | Descripción |
|---------|-------------|
| 52_ecuaciones_diferenciales.py | Versión única con todos los algoritmos |
| 52_01_euler.py | Método de Euler para dy/dt = f(t, y) |
| 52_02_runge_kutta.py | Runge-Kutta orden 4 y comparación con Euler |
| 52_03_solve_ivp.py | Resolución con scipy.integrate.solve_ivp |
| 52_04_crecimiento.py | Modelo de crecimiento exponencial (Malthus) |
| 52_05_logistico.py | Modelo logístico (capacidad de carga) |
| 52_06_sistema.py | Sistema predador-presa (Lotka-Volterra) |
| 52_07_segundo_orden.py | EDO segundo orden: oscilador armónico |
| 52_08_resumen.py | Resumen del módulo |

## Requisitos

- Python 3.x
- NumPy (sistemas lineales, 27_04, integración)
- SciPy (25_xx sistemas lineales, 31_xx integración)
- Matplotlib (27_04, 31_04, 35_05, 52_xx)
- SciPy y Matplotlib para 52_xx (ecuaciones diferenciales)

## Ejecución

Desde la raíz del proyecto (para que los imports de `datos_sistema` y `resolver_mejorado` funcionen):

```bash
python 17_Ecuaciones/25_01_original.py
python 17_Ecuaciones/25_02_mejorado.py
# ... etc.
```

O desde dentro de `17_Ecuaciones`:

```bash
cd 17_Ecuaciones
python 25_01_original.py
```

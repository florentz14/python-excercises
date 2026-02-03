# Python Exercises

Un repositorio completo de ejercicios de Python para aprender programación desde lo básico hasta conceptos más avanzados (NumPy, Pandas, Matplotlib).

## 🚀 Instalación y dependencias

**Instalar las librerías recomendadas** (camino recomendado: NumPy, Pandas, Matplotlib):

```bash
pip install -r requirements.txt
```

Incluye: `numpy`, `pandas`, `matplotlib`. Ver [CAMINO_RECOMENDADO.md](CAMINO_RECOMENDADO.md) para la ruta completa y opciones (PyTorch/TensorFlow).

---

## 📚 Contenido

### 📁 01_Variables_y_Tipos_Datos

Variables y tipos de datos (archivos separados por tema):

- **variables.py**, **complex.py** – Variables básicas y números complejos
- **list_01** … **list_10** – Listas (crear, índice, añadir, slice, comprensión, etc.)
- **tuple_01** … **tuple_14** – Tuplas (índices, slice, desempaquetado, inmutabilidad, etc.)
- **dictionary_01** … **dictionary_16** – Diccionarios (claves, get, update, anidados, etc.)
- **set_01** … **set_18** – Conjuntos (unión, intersección, diferencia, comprensión, etc.)

### 📁 02_Condicionales

Condicionales y switch-case:

- **if_01** … **if_05** – Ejemplos de if/elif/else (número, votar, nota, par/impar, login)
- **condicional_01** … **condicional_06** – if simple, else, elif, anidado, and/or, ternario
- **switch_01** … **switch_04** – Emular switch (if/elif, diccionario, match/case)
- **exercise_zodiac_simple.py**, **exercise_chinese_zodiac.py** – Zodiaco

### 📁 03_Ciclos

Ejercicios de loops (while, for, anidados, interactivos). Ver carpeta para numeración completa.

### 📁 04_Funciones

Funciones con parámetros y bucles: **exercise_01_greet.py** … **exercise_15_countdown.py** (saludos, números, áreas, tablas, listas, etc.).

### 📁 05_Estructuras_de_Datos

**matrix.py**, **matrix_operations.py**, **count.py** – Matrices y conteo.

### 📁 06_Ejercicios_Integradores

Ejercicios que combinan varios conceptos: **app.py**, **exercise_bmi.py**, **exercise_leap_year.py**, **exercise_magic_dates.py**, **exercise_roman_numeral_converter.py**, **exercise_areas.py**, etc.

### 📁 07_Lists_and_Tuples

Ejercicios de listas y tuplas en secuencia: **Part 1** (10 listas), **Part 2** (10 tuplas), **Extras** (280). Ver [07_Lists_and_Tuples/README.md](07_Lists_and_Tuples/README.md) para el orden recomendado y la tabla de contenidos.

### 📁 08_Matrices

Vectores y matrices: **Python básico** (listas) → **NumPy paso a paso**.

- Vectores: `vector_01` … `vector_06`
- Matrices: `matrix_01` … `matrix_06`
- NumPy: `numpy_01` … `numpy_08` (arrays, dot, norm, inverse, broadcasting)

Requiere: `numpy` (incluido en `requirements.txt`).

### 📁 09_Pandas

Tablas tipo Excel: DataFrames, leer CSV, filtrar, columnas.  
Archivos: `pandas_01_crear_dataframe.py` … `pandas_04_columnas.py`.  
Requiere: `pandas`.

### 📁 10_Matplotlib

Gráficas: línea, barras, dispersión.  
Archivos: `matplotlib_01_linea.py`, `matplotlib_02_barras.py`, `matplotlib_03_scatter.py`.  
Requiere: `matplotlib`.

### 📁 11_POO (Programación Orientada a Objetos)

Clases en Python (herencia, polimorfismo):

- **clase_animales.py** – Animal, Perro, Gato, Pájaro, Pez, León
- **clase_dispositivos_moviles.py** – Smartphone, Tablet, Smartwatch, EReader, etc.
- **clase_personas.py** – Persona, Estudiante, Profesor, Ingeniero, Médico, Deportista
- **clase_transporte.py** – Transporte, Automovil, Motocicleta, Bicicleta, Avión
- **clase_usuarios.py** – Usuario, Cliente, Empleado, Vendedor, Gerente, Administrador, SoporteTecnico
- **clase_usuarios_avanzada.py** – Sistema avanzado (hasheo, sesiones, roles, auditoría)
- Clases sencillas: **clase_vector.py**, **clase_matrix_numpy.py**, **clase_point2d.py**, **clase_dataset.py**, **clase_sparse_matrix.py**, etc.

### 📁 12_Pilas

Pila (LIFO): **pila_01_lista.py**, **pila_02_clase.py**, **pila_03_parentesis.py** (balanceo de paréntesis).

### 📁 13_Colas

Cola (FIFO): **cola_01_lista.py**, **cola_02_deque.py**, **cola_03_clase.py** (con `collections.deque`).

### 📁 14_Arboles

Árbol binario: **arbol_01_nodo.py**, **arbol_02_recorrido.py** (inorden, preorden, postorden), **arbol_03_altura.py**.

### 📁 15_Grafos

Grafos (lista de adyacencia): **grafo_01_lista_adyacencia.py**, **grafo_02_clase.py**, **grafo_03_bfs.py**, **grafo_04_dfs.py**.

### 📁 Baez_Module_02_Lab … 07_Lab

Módulos de laboratorio (distancias, propinas, gráficos, BMI, años bisiestos, fechas mágicas, romanos, análisis de números, nóminas, notas, barajas, cumpleaños, etc.).

---

## 💡 Estructura de aprendizaje recomendada

1. **01_Variables_y_Tipos_Datos** – Conceptos básicos  
2. **02_Condicionales** – Toma de decisiones  
3. **03_Ciclos** – Repetición de código  
4. **04_Funciones** – Funciones y modularidad  
5. **05_Estructuras_de_Datos** – Manipulación avanzada  
6. **06_Ejercicios_Integradores** – Aplicación de conceptos  
7. **07_Lists_and_Tuples** – Más práctica con listas/tuplas  
8. **08_Matrices** – Vectores, matrices, NumPy  
9. **09_Pandas** – Tablas y datos  
10. **10_Matplotlib** – Gráficas  
11. **11_POO** – Clases, herencia y polimorfismo  

Para el **camino recomendado** (NumPy → Pandas → Matplotlib → AI/tensores), ver **[CAMINO_RECOMENDADO.md](CAMINO_RECOMENDADO.md)**.

---

## 🚀 Cómo usar

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/florentz14/python-excercises.git
   cd python-excercises
   ```

2. **Instalar dependencias (recomendado para 08, 09, 10):**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar un archivo:**

   ```bash
   python 01_Variables_y_Tipos_Datos/variables.py
   python 08_Matrices/numpy_01_instalar_importar.py
   python 09_Pandas/pandas_01_crear_dataframe.py
   python 10_Matplotlib/matplotlib_01_linea.py
   ```

---

## 📝 Características

- ✅ Comentarios y docstrings en los ejercicios  
- ✅ Organización por categorías y progresión  
- ✅ Python básico + NumPy, Pandas, Matplotlib  
- ✅ Condicionales, switch (match/case), ciclos, funciones, POO, pilas, colas, árboles, grafos  

## 👨‍💻 Autor

Florentino Báez

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

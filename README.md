# Python Exercises

Un repositorio completo de ejercicios de Python para aprender programación desde lo básico hasta conceptos avanzados (NumPy, Pandas, Matplotlib, Estructuras de Datos, MySQL).

## Instalacion y Dependencias

**Crear entorno virtual e instalar dependencias:**

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

Incluye: `numpy`, `pandas`, `matplotlib`, `mysql-connector-python`, `bcrypt`, y mas.

---

## Contenido

### 01_Variables

Variables y tipos de datos:
- Variables basicas, numeros complejos
- Listas, Tuplas, Diccionarios, Conjuntos

### 02_Condicionales

Condicionales y switch-case:
- if/elif/else, operadores logicos
- match/case (Python 3.10+)

### 03_Ciclos

Ejercicios de loops:
- while, for, anidados
- break, continue, else en loops

### 04_Funciones

Funciones en Python:
- Parametros, valores por defecto
- *args, **kwargs
- Lambda, decoradores, generadores

### 05_Estructuras_de_Datos

Algoritmos y estructuras:
- Algoritmos Greedy (mochila, Kruskal, Huffman)
- Algoritmos de Strings (Rabin-Karp, KMP, Z-algorithm)
- Algoritmos Matematicos (Pascal, Euclides, Eratostenes)
- Backtracking (N-reinas, Sudoku, laberinto)
- Estructuras avanzadas (Trie, Segment Tree, Union-Find)
- Busqueda (lineal, binaria, KMP)
- Ordenamiento (Bubble, Selection, Insertion, Merge, Quick, Heap, Counting, Radix)

### 06_Ejercicios_Integradores

Ejercicios que combinan varios conceptos:
- BMI, años bisiestos, fechas magicas
- Conversor de numeros romanos
- Calculadora de areas

### 07_Lists_and_Tuples

Ejercicios extensos de listas y tuplas (300+ archivos).

### 08_Matrices

Vectores y matrices:
- Python basico (listas)
- NumPy (arrays, operaciones, broadcasting)

### 09_Pandas

Analisis de datos:
- DataFrames, leer CSV
- Filtrar, columnas, estadisticas

### 10_Matplotlib

Visualizacion:
- Graficos de linea, barras, dispersion

### 11_POO

Programacion Orientada a Objetos:
- Clases, herencia, polimorfismo
- Ejemplos: Animales, Dispositivos, Personas, Transporte, Usuarios

### 12_Pilas

Estructura de datos Pila (LIFO):
- Implementacion con lista y clase
- Parentesis balanceados, Infix a Postfix
- Undo/Redo, historial de navegador

### 13_Colas

Estructura de datos Cola (FIFO):
- Implementacion con deque
- Cola de impresion, servicio al cliente
- Round-Robin, BFS en grafos

### 14_Arboles

Arboles binarios:
- Nodos, recorridos (inorden, preorden, postorden)
- Altura, busqueda, insercion

### 15_Grafos

Grafos:
- Lista y matriz de adyacencia
- BFS, DFS, Dijkstra
- Deteccion de ciclos, ordenamiento topologico

### 16_Archivos

Manejo de archivos:
- Lectura y escritura de archivos
- JSON, CSV

### 17_Ecuaciones

Ecuaciones matematicas:
- Algebra, calculo
- SymPy para matematica simbolica

### 18_Listas_Enlazadas

Listas enlazadas:
- Simple, doble, circular
- Operaciones: reversar, fusionar, detectar ciclos

### 19_Tablas_Hash

Tablas hash:
- Chaining, Open Addressing
- Funciones hash, aplicaciones

### 20_MySQL

Base de datos MySQL/MariaDB:
- Conexion con Python
- Sistema ATM completo con base de datos
- CRUD, procedimientos almacenados

### Baez_Module_01_Lab ... 07_Lab

Modulos de laboratorio con ejercicios practicos.

---

## Estructura de Aprendizaje Recomendada

1. **01_Variables** - Conceptos basicos
2. **02_Condicionales** - Toma de decisiones
3. **03_Ciclos** - Repeticion de codigo
4. **04_Funciones** - Modularidad
5. **05_Estructuras_de_Datos** - Algoritmos
6. **06_Ejercicios_Integradores** - Aplicacion
7. **07_Lists_and_Tuples** - Practica
8. **08_Matrices** - NumPy
9. **09_Pandas** - Analisis de datos
10. **10_Matplotlib** - Visualizacion
11. **11_POO** - Clases y objetos
12. **12_Pilas** - Estructura LIFO
13. **13_Colas** - Estructura FIFO
14. **14_Arboles** - Arboles binarios
15. **15_Grafos** - Teoria de grafos
16. **18_Listas_Enlazadas** - Estructuras dinamicas
17. **19_Tablas_Hash** - Acceso O(1)
18. **20_MySQL** - Bases de datos

---

## Como Usar

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/florentz14/python-excercises.git
   cd python-excercises
   ```

2. **Crear entorno virtual:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos (opcional):**

   Crear archivo `.env` en la raiz:
   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=tu_password
   MYSQL_DATABASE=ATM_Database_Schema
   MYSQL_PORT=3306
   ```

5. **Ejecutar un archivo:**

   ```bash
   python 01_Variables/01_variables.py
   python 20_MySQL/01_connection_test.py
   ```

---

## Caracteristicas

- Comentarios y docstrings en los ejercicios
- Organizacion por categorias y progresion
- Python basico + NumPy, Pandas, Matplotlib
- Estructuras de datos: Pilas, Colas, Arboles, Grafos, Hash Tables
- Algoritmos de ordenamiento y busqueda
- Integracion con MySQL/MariaDB

## Autor

Florentino Baez

## Licencia

Este proyecto es de codigo abierto y esta disponible para uso educativo.

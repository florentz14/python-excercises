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

### 01_Variables_and_Types

Variables y tipos de datos:
- Variables basicas, numeros complejos
- Listas, Tuplas, Diccionarios, Conjuntos

### 02_Conditionals

Conditionals and switch-case:
- if/elif/else, operadores logicos
- match/case (Python 3.10+)

### 03_Loops

Loop exercises:
- while, for, anidados
- break, continue, else en loops

### 04_Functions

Functions in Python:
- Parametros, valores por defecto
- *args, **kwargs
- Lambda, decoradores, generadores

### 05_Data_Structures

Algorithms and structures:
- Algoritmos Greedy (mochila, Kruskal, Huffman)
- Algoritmos de Strings (Rabin-Karp, KMP, Z-algorithm)
- Algoritmos Matematicos (Pascal, Euclides, Eratostenes)
- Backtracking (N-reinas, Sudoku, laberinto)
- Estructuras avanzadas (Trie, Segment Tree, Union-Find)
- Busqueda (lineal, binaria, KMP)
- Ordenamiento (Bubble, Selection, Insertion, Merge, Quick, Heap, Counting, Radix)

### 06_Integrative_Exercises

Los ejercicios integradores fueron movidos a sus módulos correspondientes:
- **02_Conditionals**: BMI, año bisiesto, fechas mágicas, convertidor romano, info nacimiento/zodíaco
- **03_Loops**: Ejemplos de for y while
- **04_Functions**: Calculadora de áreas, conversión de temperatura
- **01_Variables_and_Types**: Variables, strings, tablas f-string, input
- **10_Matplotlib**: Gráficos (seno, funciones matemáticas, Turtle)

Ver `06_Integrative_Exercises/README.md` para la tabla de reubicación.

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

### 11_OOP

Object-Oriented Programming:
- Clases, herencia, polimorfismo
- Ejemplos: Animales, Dispositivos, Personas, Transporte, Usuarios

### 12_Stacks

Stack data structure (LIFO):
- Implementacion con lista y clase
- Parentesis balanceados, Infix a Postfix
- Undo/Redo, historial de navegador

### 13_Queues

Queue data structure (FIFO):
- Implementacion con deque
- Cola de impresion, servicio al cliente
- Round-Robin, BFS en grafos

### 14_Trees

Binary trees:
- Nodos, recorridos (inorden, preorden, postorden)
- Altura, busqueda, insercion

### 15_Graphs

Graphs:
- Lista y matriz de adyacencia
- BFS, DFS, Dijkstra
- Deteccion de ciclos, ordenamiento topologico

### 16_Files

File handling (merged with former 22_Files):
- Create, read, append, list directory
- Copy, move, delete, context managers (with)
- Custom context manager, CRUD with JSON

### 17_Equations

Mathematical equations:
- Algebra, calculo
- SymPy para matematica simbolica

### 18_Linked_Lists

Linked lists:
- Simple, doble, circular
- Operaciones: reversar, fusionar, detectar ciclos

### 19_Hash_Tables

Hash tables:
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

1. **01_Variables_and_Types** - Basics
2. **02_Conditionals** - Decision making
3. **03_Loops** - Code repetition
4. **04_Functions** - Modularity
5. **05_Data_Structures** - Algorithms
6. **06_Integrative_Exercises** - Índice de ejercicios reubicados en otros módulos
7. **07_Lists_and_Tuples** - Practice
8. **08_Matrices** - NumPy
9. **09_Pandas** - Data analysis
10. **10_Matplotlib** - Visualization
11. **11_OOP** - Classes and objects
12. **12_Stacks** - LIFO structure
13. **13_Queues** - FIFO structure
14. **14_Trees** - Binary trees
15. **15_Graphs** - Graph theory
16. **18_Linked_Lists** - Dynamic structures
17. **19_Hash_Tables** - O(1) access
18. **20_MySQL** - Databases

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
   python 01_Variables_and_Types/data_types/02_variables.py
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

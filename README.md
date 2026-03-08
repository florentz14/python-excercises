# Python Exercises

A complete repository of Python exercises for learning programming from basics to advanced concepts (NumPy, Pandas, Matplotlib, Data Structures, MySQL).

## Installation and Dependencies

**Create virtual environment and install dependencies:**

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

Includes: `numpy`, `pandas`, `matplotlib`, `mysql-connector-python`, `bcrypt`, and more.

---

## Recent Project Changes

- Added and expanded `06_Statistics` with 52 progressive scripts (central tendency, distributions, sampling, inference, and regression basics).
- Reorganized and expanded `09_Pandas` with sectioned exercises and real-world datasets under `data/`.
- Extended `10_Matplotlib` to a full 01-117 sequence with applied plotting examples.
- Added new batches of exercises in `02_Conditionals`, `03_Loops`, `04_Functions`, `07_Lists_and_Tuples`, and `16_Files`.
- Reorganized `11_OOP` and `18_Linked_Lists` with stronger type hints and cleaner educational progression.
- Updated file/folder naming to English across core modules and improved inline comments/docstrings for consistency.

---

## Contents

### 01_Variables_and_Types

Variables and data types:
- Basic variables, complex numbers
- Lists, Tuples, Dictionaries, Sets

### 02_Conditionals

Conditionals and switch-case:
- if/elif/else, logical operators
- match/case (Python 3.10+)

### 03_Loops

Loop exercises:
- while, for, nested loops
- break, continue, else in loops

### 04_Functions

Functions in Python:
- Parameters, default values
- *args, **kwargs
- Lambda, decorators, generators

### 05_Data_Structures

Algorithms and structures:
- Greedy algorithms (knapsack, Kruskal, Huffman)
- String algorithms (Rabin-Karp, KMP, Z-algorithm)
- Mathematical algorithms (Pascal, Euclid, Eratosthenes)
- Backtracking (N-queens, Sudoku, maze)
- Advanced structures (Trie, Segment Tree, Union-Find)
- Search (linear, binary, KMP)
- Sorting (Bubble, Selection, Insertion, Merge, Quick, Heap, Counting, Radix)

### 06_Statistics

Statistics fundamentals for analysts (52 files):
- Central tendency and dispersion
- Quantiles and summaries
- Probability and distributions
- Sampling and inference (t-tests, confidence intervals)
- Correlation, hypothesis testing, and basic regression

### 07_Lists_and_Tuples

Extensive list and tuple exercises (300+ files).

### 08_Matrices

Vectors and matrices:
- Basic Python (lists)
- NumPy (arrays, operations, broadcasting)

### 09_Pandas

Data analysis:
- DataFrames, reading CSV
- Filtering, columns, statistics

### 10_Matplotlib

Data visualization (117 files, sequence 01-117):
- Pyplot, points, markers, line styles
- Labels, grids, subplots
- Scatter, bar, histogram, pie charts
- Applied data: Iris, Pokémon, wine, crime, Euro 2012, Auto MPG
- Special charts: Turtle, sine, mathematical functions

### 11_OOP

Object-oriented programming (with type hints):
- **Conceptual path (01-27)**: Basic classes, `__init__`, attributes, `__str__`/`__repr__`, encapsulation, getters/setters, `@property`, inheritance, polymorphism, duck typing, magic methods (`__len__`, `__eq__`), operator overloading, `@classmethod`, `@staticmethod`, `@dataclass`, abstract classes, composition
- **Applications (21-27)**: Person, Rectangle, Account, Shape, Inventory, Vehicle, Library
- **Examples (28-54)**: Animals, Dataset, Devices, Matrix, People, Point, Transport, Users, Vector, etc.

### 12_Stacks

Stack data structure (LIFO):
- List and class implementation
- Balanced parentheses, Infix to Postfix
- Undo/Redo, browser history

### 13_Queues

Queue data structure (FIFO):
- Implementation with deque
- Print queue, customer service
- Round-Robin, BFS on graphs

### 14_Trees

Binary trees:
- Nodes, traversals (inorder, preorder, postorder)
- Height, search, insertion

### 15_Graphs

Graphs:
- Adjacency list and matrix
- BFS, DFS, Dijkstra
- Cycle detection, topological sort

### 16_Files

File handling:
- Create, read, append, list directory
- Copy, move, delete, context managers (`with`)
- Custom context manager, CRUD with JSON
- Reading large files (streaming), `seek`/`tell`
- Binary files, CSV, temporary files
- Permissions, pathlib, recursive directory traversal

### 17_Equations

Numerical methods and equations (70 files):
- Linear systems, nonlinear equations
- Numerical integration, numerical differentiation
- Riemann sums, trapezoid, Simpson
- Newton-Raphson, interpolation (Lagrange, Newton)
- Linear and polynomial regression
- Computational geometry (distances, polygon area, convex hull, intersections)
- Differential equations (Euler, Runge-Kutta, solve_ivp)

### 18_Linked_Lists

Linked lists (with type hints):
- Single, doubly, circular
- Operations: insert, delete, reverse
- Find middle, cycle detection (Floyd)
- Merge sorted lists, remove duplicates
- Intersection, k-th from end
- Partition, LRU Cache (doubly linked list + hashmap)

### 19_Hash_Tables

Hash tables:
- Chaining, Open Addressing
- Hash functions, applications

### 20_MySQL

MySQL/MariaDB database:
- Connection with Python
- Complete ATM system with database
- CRUD, stored procedures

### 21_Machine_Learning

Machine learning foundations:
- Flattened structure for easier navigation
- Intro workflows and practical examples
- Includes support files and dependencies (e.g., `xgboost`)

### 22_Exceptions

Exception handling:
- try/except, multiple exception types
- Exception, else, finally, raise
- logging.exception

### Baez_Module_01_Lab ... 07_Lab

Laboratory modules with practical exercises.

---

## Recommended Learning Path

This path is pedagogical and does not follow folder numbering.

1. **01_Variables_and_Types** - Data types, lists, dictionaries, sets
2. **02_Conditionals** - Decision making, match/case
3. **03_Loops** - Loops (while, for, nested)
4. **04_Functions** - Functions, parameters, decorators
5. **07_Lists_and_Tuples** - Intensive collection and sequence practice
6. **16_Files** - File I/O, JSON/CSV, context managers, and `pathlib`
7. **22_Exceptions** - Error handling patterns for robust scripts
8. **11_OOP** - Classes, encapsulation, inheritance, and composition
9. **12_Stacks** - LIFO structure and classic applications
10. **13_Queues** - FIFO structure, BFS, and scheduling use cases
11. **18_Linked_Lists** - Singly/doubly/circular lists and pointer techniques
12. **19_Hash_Tables** - Hashing strategies and lookup optimization
13. **14_Trees** - Tree traversals, insertion/search, and structural reasoning
14. **15_Graphs** - Graph modeling, BFS/DFS, shortest paths
15. **05_Data_Structures** - Integrated algorithms: sorting, search, greedy, backtracking
16. **06_Statistics** - Statistical foundations for data analysis
17. **08_Matrices** - Arrays/matrices with Python and NumPy
18. **09_Pandas** - Data wrangling and exploratory analysis
19. **10_Matplotlib** - Data visualization and plotting practice
20. **17_Equations** - Numerical methods and computational math
21. **20_MySQL** - Relational databases with Python
22. **21_Machine_Learning** - Intro ML workflows after math/data foundations

---

## How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/florentz14/python-excercises.git
   cd python-excercises
   ```

2. **Create virtual environment:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database (optional):**

   Create `.env` file in the root:
   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=your_password
   MYSQL_DATABASE=ATM_Database_Schema
   MYSQL_PORT=3306
   ```

5. **Run a file:**

   ```bash
   python 01_Variables_and_Types/data_types/02_variables.py
   python 20_MySQL/01_connection_test.py
   ```

---

## Features

- Comments and docstrings in exercises
- **Type hints** in OOP and Linked Lists modules
- Organized by category and progression
- Basic Python + NumPy, Pandas, Matplotlib, Seaborn
- Data structures: Stacks, Queues, Trees, Graphs, Linked Lists, Hash Tables
- Sorting and search algorithms
- MySQL/MariaDB integration

## Author

Florentino Baez

## License

This project is open source and available for educational use.

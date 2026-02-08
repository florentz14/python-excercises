# Set Theory Exercises - Python 3.14 Solutions

This repository contains complete solutions to 12 set theory exercises implemented in Python 3.14. Each exercise is thoroughly commented in English and demonstrates fundamental concepts of set theory.

## 📚 Exercise List

### Basic Concepts
1. **Exercise 01** - Notation and Elements
   - Set membership (∈, ∉)
   - Subset operations (⊂)
   - Boolean checks

2. **Exercise 02** - Set Comprehension
   - Creating sets with conditions
   - List comprehension syntax
   - Filtering elements

3. **Exercise 03** - Union of Sets
   - Union operation (∪)
   - Combining sets
   - Counting elements

### Core Operations
4. **Exercise 04** - Intersection of Sets
   - Intersection operation (∩)
   - Finding common elements
   - Empty set checks

5. **Exercise 05** - Difference of Sets
   - Set difference (-)
   - Non-commutative operations
   - Symmetric difference

6. **Exercise 06** - Complement of Sets
   - Complement operation (')
   - Universal sets
   - Double complement law

### Advanced Topics
7. **Exercise 07** - Subsets
   - Finding all subsets
   - Power set generation
   - 2^n formula

8. **Exercise 08** - Combined Operations
   - Multiple operations
   - Order of operations
   - Parentheses usage

9. **Exercise 09** - Cardinality
   - Set size calculations
   - Inclusion-exclusion principle
   - Disjoint set properties

### Applied Problems
10. **Exercise 10** - Venn Diagram Problem
    - Real-world application
    - Student enrollment problem
    - Visual representation

### Bonus Exercises
11. **Exercise 11** - Cartesian Product
    - Ordered pairs
    - A × B notation
    - Non-commutative property

12. **Exercise 12** - Disjoint Sets
    - Intersection tests
    - Empty set checks
    - Set relationships

## 🚀 How to Run

### Run Individual Exercises
```bash
python3 exercise_01_notation_and_elements.py
python3 exercise_02_set_comprehension.py
# ... and so on
```

### Run All Exercises at Once
```bash
python3 run_all_exercises.py
```

This will execute all 12 exercises in sequence with clear output formatting.

## 📋 Requirements

- Python 3.14 or higher
- No external libraries required (uses only standard library)

## 🔧 Python Set Operations Reference

| Operation | Symbol | Python Syntax | Alternative |
|-----------|--------|---------------|-------------|
| Union | ∪ | `A \| B` | `A.union(B)` |
| Intersection | ∩ | `A & B` | `A.intersection(B)` |
| Difference | - | `A - B` | `A.difference(B)` |
| Symmetric Difference | Δ | `A ^ B` | `A.symmetric_difference(B)` |
| Subset | ⊆ | `A <= B` | `A.issubset(B)` |
| Proper Subset | ⊂ | `A < B` | - |
| Superset | ⊇ | `A >= B` | `A.issuperset(B)` |
| Membership | ∈ | `x in A` | - |
| Non-membership | ∉ | `x not in A` | - |
| Cardinality | \|A\| | `len(A)` | - |

## 📖 Key Concepts Covered

### Set Properties
- **Uniqueness**: Sets contain no duplicate elements
- **Unordered**: Elements have no specific order
- **Mutable**: Sets can be modified (add/remove elements)
- **Heterogeneous**: Can contain different data types

### Mathematical Laws
- **Commutative Law**: A ∪ B = B ∪ A, A ∩ B = B ∩ A
- **Associative Law**: (A ∪ B) ∪ C = A ∪ (B ∪ C)
- **Distributive Law**: A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
- **De Morgan's Laws**: (A ∪ B)' = A' ∩ B', (A ∩ B)' = A' ∪ B'
- **Double Complement**: (A')' = A

### Formulas
- **Inclusion-Exclusion**: |A ∪ B| = |A| + |B| - |A ∩ B|
- **Power Set Size**: |P(A)| = 2^|A|
- **Cartesian Product Size**: |A × B| = |A| × |B|

## 💡 Learning Objectives

After completing these exercises, you will understand:
- How to create and manipulate sets in Python
- Fundamental set operations and their properties
- How to solve real-world problems using set theory
- The mathematical foundations of set theory
- Efficient Python set methods and syntax

## 📝 Code Style

All code follows these conventions:
- Comprehensive English comments
- Clear variable names
- Docstrings for functions
- Step-by-step explanations
- Visual output formatting
- Educational print statements

## 🎓 Educational Use

These exercises are perfect for:
- Computer Science students learning discrete mathematics
- Self-learners studying set theory
- Teachers looking for coding examples
- Anyone wanting to understand Python sets

## 📄 File Structure

```
set_exercises/
│
├── exercise_01_notation_and_elements.py
├── exercise_02_set_comprehension.py
├── exercise_03_union.py
├── exercise_04_intersection.py
├── exercise_05_difference.py
├── exercise_06_complement.py
├── exercise_07_subsets.py
├── exercise_08_combined_operations.py
├── exercise_09_cardinality.py
├── exercise_10_venn_diagram.py
├── exercise_11_cartesian_product.py
├── exercise_12_disjoint_sets.py
├── run_all_exercises.py
└── README.md
```

## 🤝 Contributing

Feel free to:
- Add more exercises
- Improve explanations
- Fix any issues
- Suggest enhancements

## 📚 Additional Resources

- [Python Set Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Set Theory on Wikipedia](https://en.wikipedia.org/wiki/Set_theory)
- [Discrete Mathematics Resources](https://en.wikipedia.org/wiki/Discrete_mathematics)

---

**Created for educational purposes** | Python 3.14+ | MIT License

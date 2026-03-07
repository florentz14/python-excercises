# 11_OOP

Object-Oriented Programming in Python - Conceptual Learning Path

This module provides a comprehensive, concept-based introduction to Object-Oriented Programming (OOP) in Python. Instead of example-based classes, it focuses on systematic learning of OOP principles through 27 files organized into 8 conceptual blocks.

## Learning Structure

### 1. Fundamentals (Files 01-07)

Basic OOP concepts and class creation.

| File                       | Concept               | Description                                      |
| -------------------------- | --------------------- | ------------------------------------------------ |
| `01_basic_class.py`        | Basic Classes         | Class definition, object creation, basic methods |
| `02_init_constructor.py`   | Constructors          | `__init__` method, initialization, validation    |
| `03_attributes_methods.py` | Attributes & Methods  | Instance/class attributes, method definitions    |
| `04_str_repr.py`           | String Representation | `__str__` and `__repr__` magic methods           |
| `05_private_attributes.py` | Encapsulation         | Private attributes, name mangling                |
| `06_getters_setters.py`    | Manual Properties     | Getter/setter methods for encapsulation          |
| `07_property_decorator.py` | @property Decorator   | Python's property decorator for clean access     |

### 2. Inheritance (Files 08-10)

Building class hierarchies and code reuse.

| File                         | Concept              | Description                              |
| ---------------------------- | -------------------- | ---------------------------------------- |
| `08_inheritance_basic.py`    | Basic Inheritance    | Parent/child classes, method inheritance |
| `09_method_override.py`      | Method Overriding    | Overriding parent methods, super() calls |
| `10_multiple_inheritance.py` | Multiple Inheritance | Inheriting from multiple classes, MRO    |

### 3. Polymorphism (Files 11-12)

Different behaviors for the same interface.

| File                 | Concept      | Description                            |
| -------------------- | ------------ | -------------------------------------- |
| `11_polymorphism.py` | Polymorphism | Same method, different implementations |
| `12_duck_typing.py`  | Duck Typing  | Python's dynamic typing approach       |

### 4. Magic Methods (Files 13-16)

Special methods for operator overloading and behavior customization.

| File                         | Concept                | Description                                |
| ---------------------------- | ---------------------- | ------------------------------------------ |
| `13_len_method.py`           | `__len__` Method       | Custom length behavior                     |
| `14_eq_method.py`            | `__eq__` Method        | Equality comparison customization          |
| `15_operator_overloading.py` | Operator Overloading   | Custom operators (+, -, \*, etc.)          |
| `16_classmethod.py`          | @classmethod Decorator | Class methods and alternative constructors |

### 5. Class Methods (Files 17-18)

Advanced method types and decorators.

| File                 | Concept                 | Description                       |
| -------------------- | ----------------------- | --------------------------------- |
| `17_staticmethod.py` | @staticmethod Decorator | Static methods, utility functions |
| `18_dataclasses.py`  | @dataclass Decorator    | Automatic method generation       |

### 6. Advanced Concepts (Files 19-20)

Abstract classes and composition patterns.

| File                     | Concept                    | Description                       |
| ------------------------ | -------------------------- | --------------------------------- |
| `19_abstract_classes.py` | Abstract Base Classes      | ABC, abstract methods, interfaces |
| `20_composition.py`      | Composition vs Inheritance | Building objects from components  |

### 7. Practical Applications (Files 21-26)

Real-world OOP implementations.

| File              | Concept           | Description                            |
| ----------------- | ----------------- | -------------------------------------- |
| `21_person.py`    | Person Class      | Complete person management system      |
| `22_rectangle.py` | Rectangle Class   | Geometric shapes with properties       |
| `23_account.py`   | Bank Account      | Financial transactions and validation  |
| `24_shape.py`     | Shape Hierarchy   | Inheritance and polymorphism in shapes |
| `25_inventory.py` | Inventory System  | Product and stock management           |
| `26_vehicle.py`   | Vehicle Hierarchy | Multiple inheritance and mixins        |

### 8. Integrative Exercises (File 27)

Comprehensive real-world system.

| File            | Concept            | Description                                   |
| --------------- | ------------------ | --------------------------------------------- |
| `27_library.py` | Library Management | Complete library system with all OOP concepts |

### 9. Example Classes (Files 28-54)

Additional example-based classes for practice.

| File | Concept |
|------|---------|
| `28_animals.py` | Animals (inheritance) |
| `29_dataset.py` | Dataset class |
| `30_devices.py` | Mobile devices |
| `31_matrix.py` | Matrix class |
| `32_matrix_numpy.py` | Matrix with NumPy |
| `33_people.py` | People class |
| `34_point.py` | Point 2D |
| `35_sparse_matrix.py` | Sparse matrix |
| `36_transport.py` | Transport class |
| `37_users.py` | Users class |
| `38_advanced_users.py` | Advanced users |
| `39_vector.py` | Vector class |
| `40_vector_numpy.py` | Vector with NumPy |
| `41_person.py` | Person (basic) |
| `42_rectangle.py` | Rectangle |
| `43_book.py` | Book |
| `44_account.py` | Bank account |
| `45_point.py` | Point (2D coords) |
| `46_inheritance.py` | Parent → Child |
| `47_atm.py` | ATM |
| `48_circle.py` | Circle (getter/setter) |
| `49_product.py` | Product |
| `50_student.py` | Student |
| `51_counter.py` | Counter |
| `52_triangle.py` | Triangle |
| `53_contact.py` | Contact |
| `54_dog.py` | Dog (inheritance) |

## Key OOP Concepts Covered

### Core Principles

- **Encapsulation**: Data hiding and controlled access
- **Inheritance**: Code reuse through class hierarchies
- **Polymorphism**: Same interface, different implementations
- **Abstraction**: Hiding complexity, focusing on essentials

### Python-Specific Features

- Magic methods (`__init__`, `__str__`, `__eq__`, etc.)
- Property decorators (`@property`, `@classmethod`, `@staticmethod`)
- Data classes (`@dataclass`)
- Abstract base classes (ABC)
- Multiple inheritance and MRO
- Duck typing

### Design Patterns

- Factory pattern (alternative constructors)
- Composition over inheritance
- Strategy pattern (polymorphic behavior)
- Template method pattern (abstract classes)

## Learning Approach

Each file follows a consistent structure:

1. **Concept Explanation**: Clear description of the OOP concept
2. **Code Examples**: Practical implementations
3. **Demonstration**: Working examples with output
4. **Key Takeaways**: Summary of important points

## Prerequisites

- Basic Python syntax
- Understanding of functions and variables
- Familiarity with data structures (lists, dictionaries)

## Running the Examples

All files are self-contained and can be run independently:

```bash
python 01_basic_class.py
python 02_init_constructor.py
# ... etc
```

Each file includes a `if __name__ == "__main__":` block with demonstrations.

## Progression Guide

Start with fundamentals (01-07), then move through inheritance and polymorphism. Study magic methods and advanced decorators, then tackle abstract classes and composition. Finally, explore the practical applications and the comprehensive library system.

This structure ensures a thorough understanding of OOP principles while building practical Python programming skills.

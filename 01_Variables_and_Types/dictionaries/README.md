# Dictionaries - Complete Guide

A comprehensive collection of 26 programs covering everything about Python dictionaries: from basic operations to advanced types and performance optimization.

## Files (26 programs)

### Tutorials (01-16)

| #  | File | Topic |
|----|------|-------|
| 01 | `01_create_and_display.py` | Creating dictionaries and displaying them |
| 02 | `02_access_by_key.py` | Accessing values by key |
| 03 | `03_get_method.py` | Using `.get()` for safe access with defaults |
| 04 | `04_add_modify.py` | Adding and modifying key-value pairs |
| 05 | `05_remove_items.py` | Removing items (`del`, `pop`, `popitem`) |
| 06 | `06_loop.py` | Looping through dictionaries |
| 07 | `07_loop_items.py` | Looping with `.items()`, `.keys()`, `.values()` |
| 08 | `08_keys_values.py` | Working with keys and values views |
| 09 | `09_check_key_exists.py` | Checking if a key exists (`in`, `.get()`) |
| 10 | `10_update.py` | Merging dictionaries with `.update()` |
| 11 | `11_copy.py` | Shallow copy vs deep copy |
| 12 | `12_clear.py` | Clearing a dictionary |
| 13 | `13_nested.py` | Nested dictionaries (dicts inside dicts) |
| 14 | `14_comprehension.py` | Dictionary comprehension |
| 15 | `15_list_tuples_to_dict.py` | Converting lists/tuples to dictionaries |
| 16 | `16_setdefault.py` | Using `.setdefault()` |

### Exercises (17-26)

| #  | File | Topic |
|----|------|-------|
| 17 | `17_basic_operations.py` | Basic dictionary operations (create, access, modify, remove) |
| 18 | `18_dictionary_methods.py` | Dictionary methods (`keys`, `values`, `items`, `update`, `fromkeys`) |
| 19 | `19_nested_dictionaries.py` | Nested dictionaries and hierarchical data |
| 20 | `20_dict_comprehension.py` | Dictionary comprehension (filter, transform, nested) |
| 21 | `21_word_frequency.py` | Word frequency counter with `collections.Counter` |
| 22 | `22_grade_manager.py` | Student grade management system (CRUD, statistics) |
| 23 | `23_json_dictionaries.py` | Working with JSON and dictionaries (read, write, API) |
| 24 | `24_contact_book.py` | Contact book application (CRUD, persistent storage) |
| 25 | `25_advanced_dict_types.py` | Advanced types: `defaultdict`, `OrderedDict`, LRU cache |
| 26 | `26_performance.py` | Performance benchmarks and best practices |

## Quick Start

```bash
# Run individual programs
python 01_create_and_display.py
python 17_basic_operations.py
```

## Requirements

- **Python 3.10+**
- **Standard Library Only** - No external dependencies

Modules used: `collections`, `json`, `time`, `sys`

## Dictionary Basics

### Creating Dictionaries

```python
# Empty dictionary
empty = {}
empty = dict()

# With initial values
person = {"name": "Alice", "age": 30}

# From lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
```

### Common Operations

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Access | `dict[key]` | Get value (raises KeyError if missing) |
| Safe access | `dict.get(key, default)` | Get value with default |
| Add/Update | `dict[key] = value` | Set key-value pair |
| Delete | `del dict[key]` | Remove key-value pair |
| Remove & return | `dict.pop(key)` | Remove and return value |
| Check existence | `key in dict` | Test if key exists |
| Length | `len(dict)` | Number of key-value pairs |

### Iteration

```python
# Iterate over keys
for key in my_dict:
    print(key)

# Iterate over values
for value in my_dict.values():
    print(value)

# Iterate over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

## Key Concepts

### 1. Keys Must Be Immutable

**Valid keys:** Strings, Numbers, Tuples, Booleans

**Invalid keys:** Lists, Dictionaries, Sets

### 2. Hash Table Implementation

Dictionaries use hash tables for O(1) average lookup time:
- **Lookup**: O(1)
- **Insert**: O(1)
- **Delete**: O(1)

### 3. Order Preservation

Since Python 3.7+, dictionaries maintain insertion order.

### 4. Dictionary Methods

```python
# Getting data
.keys()                    # View of all keys
.values()                  # View of all values
.items()                   # View of (key, value) pairs
.get(key, default)         # Safe access

# Modifying
.update(other)             # Merge dictionaries
.setdefault(key, default)  # Get or set default
.pop(key)                  # Remove and return
.popitem()                 # Remove and return last item
.clear()                   # Remove all items

# Copying
.copy()                    # Shallow copy
```

## Learning Path

### Beginner (01-09)
Basic creation, access, modification, iteration, and key checking.

### Intermediate (10-20)
Update, copy, clear, nested dicts, comprehensions, conversions, setdefault, and practical exercises.

### Advanced (21-26)
Word frequency, grade manager, JSON integration, contact book, advanced types, and performance.

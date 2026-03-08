# Dictionaries - Complete Guide

A comprehensive collection of 57 programs organized by category and level: from basic operations to advanced types and performance optimization.

## Files (57 programs) - Basic → Complex

### Level 1: Fundamentals (01-12)

| #   | File               | Topic                                           |
| --- | ------------------ | ----------------------------------------------- |
| 01  | `01_create.py`     | Creating and displaying dictionaries            |
| 02  | `02_access.py`     | Accessing values by key                         |
| 03  | `03_get.py`        | `.get()` for safe access with defaults          |
| 04  | `04_add_modify.py` | Adding and modifying key-value pairs            |
| 05  | `05_remove.py`     | Removing items (`del`, `pop`, `popitem`)        |
| 06  | `06_loop.py`       | Looping through dictionaries                    |
| 07  | `07_loop_items.py` | Looping with `.items()`, `.keys()`, `.values()` |
| 08  | `08_keys_values.py`| Working with keys and values views              |
| 09  | `09_check_key.py`  | Checking if a key exists (`in`, `.get()`)       |
| 10  | `10_update.py`     | Merging dictionaries with `.update()`           |
| 11  | `11_copy.py`       | Shallow copy vs deep copy                       |
| 12  | `12_clear.py`      | Clearing a dictionary                           |

### Level 2: Nested Dictionaries (13-20)

| #   | File                  | Topic                                   |
| --- | --------------------- | --------------------------------------- |
| 13  | `13_nested_basic.py`  | Basic nested structure                  |
| 14  | `14_nested_access.py` | Accessing with key chaining             |
| 15  | `15_nested_iterate.py`| Iterating with keys, values, items      |
| 16  | `16_nested_enumerate.py`| enumerate for numbered output         |
| 17  | `17_nested_to_lists.py`| Converting views to lists               |
| 18  | `18_nested_modify.py` | Modifying nested values                 |
| 19  | `19_nested_deep.py`   | Deeply nested (3+ levels)               |
| 20  | `20_nested_mixed.py`  | Mixed structures (dict + lists)         |

### Level 3: Conversion & Creation (21-24)

| #   | File                  | Topic                                   |
| --- | --------------------- | --------------------------------------- |
| 21  | `21_list_to_dict.py`  | Converting lists/tuples to dicts         |
| 22  | `22_setdefault.py`    | Using `.setdefault()`                    |
| 23  | `23_fromkeys.py`      | Creating dicts with fromkeys()           |
| 24  | `24_comprehension.py` | Basic dictionary comprehension          |

### Level 4: Dictionary Comprehension (25-34)

| #   | File                    | Topic                                   |
| --- | ----------------------- | --------------------------------------- |
| 25  | `25_comp_basic.py`      | Basic squares                            |
| 26  | `26_comp_filter.py`     | Conditional filter                       |
| 27  | `27_comp_cond_vals.py` | Conditional values (ternary)              |
| 28  | `28_comp_enumerate.py` | Using enumerate()                        |
| 29  | `29_comp_from_lists.py`| From two lists with zip()                 |
| 30  | `30_comp_grades.py`     | Grade statistics                         |
| 31  | `31_comp_nested.py`     | Nested (multiplication table)            |
| 32  | `32_comp_strings.py`   | String manipulation                      |
| 33  | `33_comp_swap.py`      | Swap keys and values                     |
| 34  | `34_comp_transform.py` | Transform existing dict                  |

### Level 5: Operations (35-42)

| #   | File                  | Topic                                   |
| --- | --------------------- | --------------------------------------- |
| 35  | `35_merge.py`         | Merge dicts (Python 3.9+ \|)             |
| 36  | `36_remove_compare.py`| Compare del, pop, popitem, clear        |
| 37  | `37_reverse.py`       | Reverse keys and values                 |
| 38  | `38_sort.py`          | Sort by keys and values                 |
| 39  | `39_grouping.py`      | Group values in dict of lists           |
| 40  | `40_invert.py`        | Build grouped dicts from records        |
| 41  | `41_unpacking.py`     | Dictionary unpacking with \*\*           |
| 42  | `42_safe_nested.py`   | Safe access to nested dicts             |

### Level 6: Concepts (43-46)

| #   | File                  | Topic                                   |
| --- | --------------------- | --------------------------------------- |
| 43  | `43_lookup.py`        | Dictionaries as lookup tables           |
| 44  | `44_dispatch.py`      | Function dispatch with dicts            |
| 45  | `45_hashable.py`      | Hashable vs unhashable keys             |
| 46  | `46_equality.py`      | Dictionary equality and comparison      |

### Level 7: Simple Examples (47-49)

| #   | File                  | Topic                                   |
| --- | --------------------- | --------------------------------------- |
| 47  | `47_simple_loop.py`   | Simple loop examples                    |
| 48  | `48_simple_nested.py` | Simple nested examples                  |
| 49  | `49_nested_loop.py`   | Nested loop examples                    |

### Level 8: Frequency & Counters (50-51)

| #   | File                  | Topic                                   |
| --- | --------------------- | --------------------------------------- |
| 50  | `50_word_freq.py`     | Word frequency with Counter             |
| 51  | `51_freq_counter.py`  | Frequency counting with plain dict     |

### Level 9: Applications (52)

| #   | File                 | Topic                                   |
| --- | -------------------- | --------------------------------------- |
| 52  | `52_json.py`         | Working with JSON (read, write, API)    |

### Level 10: Advanced (53-57)

| #   | File                    | Topic                                   |
| --- | ----------------------- | --------------------------------------- |
| 53  | `53_basic_ops.py`       | Integrated basic operations             |
| 54  | `54_methods.py`        | Dictionary methods overview             |
| 55  | `55_nested_full.py`    | Full nested example (company, grades)   |
| 56  | `56_advanced_types.py` | defaultdict, OrderedDict, LRU cache    |
| 57  | `57_performance.py`    | Performance benchmarks                  |

**Note:** GradeManager and ContactBook (OOP applications) moved to `11_OOP/55_grade_manager.py` and `11_OOP/56_contact_book.py`

## Quick Start

```bash
# Run from basic to complex
python 01_create.py
python 55_basic_ops.py
```

## Requirements

- **Python 3.10+**
- **Standard Library Only** - No external dependencies

Modules used: `collections`, `json`, `time`, `sys`

## Learning Path

| Level | Range | Focus |
| ----- | ----- | ----- |
| Beginner | 01-12 | Create, access, modify, iterate |
| Intermediate | 13-24 | Nested, conversion, comprehension |
| Advanced | 25-42 | Comp variations, operations |
| Expert | 43-59 | Concepts, apps, performance |

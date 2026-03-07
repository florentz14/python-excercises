# 22_Exceptions

Exception handling in Python: try/except, multiple handlers, else, finally, raise.

## Files

| File | Content |
|------|---------|
| `01_exceptions_chapter_tutorial.py` | try/except, multiple types, Exception, else/finally/raise |
| `02_exceptions_reference_and_exercises.py` | Reference, common exceptions, Ex 1 (list), Ex 2 (dict) |
| `03_file_exceptions.py` | FileNotFoundError, PermissionError, reading files safely |
| `04_custom_exceptions.py` | Custom exception classes, inheritance, raising custom errors |
| `05_validation_exceptions.py` | Input validation: age, email, positive number, non-empty string |
| `06_exception_chaining.py` | raise from, exception chaining, cause and context |
| `07_context_manager_exceptions.py` | Exceptions in with blocks, suppress, redirect |

## 01 - Sections

1. **try / except** - Divide by zero
2. **Multiple exception types** - IndexError, ValueError
3. **Generic Exception** - Catch any error, logging.exception
4. **else, finally, raise** - Sum with validation

## 02 - Content

- try/except/finally, raise
- Common exceptions: TypeError, ValueError, NameError, IndexError, KeyError
- **Exercise 1**: Access list by user index (IndexError, ValueError)
- **Exercise 2**: Access dict by key (KeyError)

## 03 - File Exceptions

- FileNotFoundError when opening missing files
- PermissionError for restricted access
- Safe file reading with multiple exception handlers

## 04 - Custom Exceptions

- Define custom exception classes (inherit from Exception)
- Raise with custom messages
- Catch specific custom types

## 05 - Validation Exceptions

- validate_age(), validate_email(), validate_positive(), validate_non_empty()
- Raise ValueError with descriptive messages
- Reusable validation helpers

## 06 - Exception Chaining

- raise ... from ... to chain cause
- __cause__ and __context__ attributes
- When to use chaining vs simple raise

## 07 - Context Manager Exceptions

- Exceptions inside with blocks
- contextlib.suppress to ignore specific exceptions
- Redirecting stderr for cleaner output

## Run

```bash
python 01_exceptions_chapter_tutorial.py
python 02_exceptions_reference_and_exercises.py        # Demo mode
python 02_exceptions_reference_and_exercises.py -i     # Interactive mode
python 03_file_exceptions.py
python 04_custom_exceptions.py
python 05_validation_exceptions.py
python 06_exception_chaining.py
python 07_context_manager_exceptions.py
```

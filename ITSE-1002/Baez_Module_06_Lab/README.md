# Baez_Module_06_Lab

Module 6 Lab: Files and data processing.

## Note on try-except Blocks

A `try-except` block has been added to all programs in this module. **Reasons:**

1. **Input validation**: `float()` and `int()` raise `ValueError` when the user enters non-numeric input (e.g., letters or empty input). The try-except catches this and displays a friendly error message instead of crashing.
2. **Robustness**: Prevents the program from terminating unexpectedly due to invalid or unexpected input.
3. **User experience**: Prompts the user to re-enter valid data rather than exiting with a traceback.

## Files

| File | Content |
|------|---------|
| `01_number_analysis.py` | Number analysis |
| `02_employees_pay.py` | Employee pay |
| `03_exam_grades.py` | Exam grades |

## Citations

### `01_number_analysis.py`
- **List Operations in Python**: min(), max(), sum() functions for list analysis; List methods: append(). Source: [Python Documentation - Built-in Functions](https://docs.python.org/3/library/functions.html)
- **Statistical Calculations**: Average = Sum of values / Number of values. Source: Standard statistical methods

### `02_employees_pay.py`
- **List Operations in Python**: List methods: append(); sum() function for totaling list values. Source: [Python Documentation - Built-in Functions](https://docs.python.org/3/library/functions.html)
- **Payroll Calculation**: Gross Pay = Hours Worked × Hourly Rate. Source: Standard payroll calculation formula

### `03_exam_grades.py`
- **List Operations in Python**: min() function for list analysis; List methods: append(), remove(), copy(). Source: [Python Documentation - Built-in Functions](https://docs.python.org/3/library/functions.html)
- **Statistical Calculations**: Average = Sum of values / Number of values; Dropping lowest score before averaging. Source: Standard statistical methods for grade calculation

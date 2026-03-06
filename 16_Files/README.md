# 16_Files - File handling in Python

Merged content from 16_Archivos and 22_Files. File operations: create, read, append,
list directories, copy, move, delete, and context managers.

All programs and comments are in English.

## Structure

| # | File                          | Description                                |
|---|-------------------------------|--------------------------------------------|
| 01 | `01_write.py`                 | Create and write to files                  |
| 02 | `02_read.py`                  | Read files (read, readline, readlines)    |
| 03 | `03_append.py`                | Append content to the end                  |
| 04 | `04_read_lines.py`            | Read line by line (students.txt)           |
| 05 | `05_exists.py`                | Check if file or folder exists             |
| 06 | `06_list_directory.py`       | List directory contents                    |
| 07 | `07_delete.py`                | Delete files                               |
| 08 | `08_copy_move.py`             | Copy and move files                        |
| 09 | `09_with_context.py`          | Context manager (with)                     |
| 10 | `10_read_modify.py`           | Read, modify a line, write back             |
| 11 | `11_context_manager_logger.py`| Custom context manager (logger)             |
| 12 | `12_crud_employees.py`        | CRUD employees (JSON)                      |

## Data files

- `students.txt` - Used by 04 and 10 (created by 01_write or provided as seed)
- `employees.json` - Created by 12_crud_employees

## Suggested order

**Basic flow:** 01 → 02 → 03 → 04 → 05 → 09 → 10

**Full flow:** 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12

## How to run

```bash
cd 16_Files
python 01_write.py
python 02_read.py
# ...
```

## Requirements

- Python 3.10+ (for type hints)
- No external libraries required

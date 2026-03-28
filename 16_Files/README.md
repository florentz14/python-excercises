# 16_Files - File handling in Python

**Created:** 2026-02-03 (filesystem date for this file)

Comprehensive file operations in Python: create, read, append, modify, copy, move,
delete, permissions, binary files, CSV, temporary files, pathlib, and directory traversal.

All programs and comments are in English.

## Structure

| #   | File                             | Description                            |
| --- | -------------------------------- | -------------------------------------- |
| 01  | `01_write.py`                    | Create and write to files              |
| 02  | `02_read.py`                     | Read files (read, readline, readlines) |
| 03  | `03_append.py`                   | Append content to the end              |
| 04  | `04_read_lines.py`               | Read line by line (students.txt)       |
| 05  | `05_exists.py`                   | Check if file or folder exists         |
| 06  | `06_list_directory.py`           | List directory contents                |
| 07  | `07_delete.py`                   | Delete files                           |
| 08  | `08_copy_move.py`                | Copy and move files                    |
| 09  | `09_with_context.py`             | Context manager (with)                 |
| 10  | `10_read_modify.py`              | Read, modify a line, write back        |
| 11  | `11_context_manager_logger.py`   | Custom context manager (logger)        |
| 12  | `12_crud_employees.py`           | CRUD employees (JSON)                  |
| 13  | `13_read_large_file_stream.py`   | Efficient large file reading           |
| 14  | `14_file_seek_tell.py`           | File pointer operations (seek/tell)    |
| 15  | `15_binary_files.py`             | Working with binary files              |
| 16  | `16_csv_files.py`                | CSV reading and writing                |
| 17  | `17_temp_files.py`               | Temporary files with tempfile          |
| 18  | `18_file_permissions.py`         | File permissions (chmod)               |
| 19  | `19_pathlib_basics.py`           | Modern file handling with pathlib      |
| 20  | `20_recursive_directory_walk.py` | Directory traversal with os.walk       |

## File Exercises (21-30)

| #   | File                              | Description                                                  |
| --- | --------------------------------- | ------------------------------------------------------------ |
| 21  | `21_multiplication_table_save.py` | Ask 1-10, save multiplication table to table-n.txt           |
| 22  | `22_multiplication_table_read.py` | Ask 1-10, read table-n.txt (error if missing)                |
| 23  | `23_multiplication_table_read_line.py` | Ask n, m 1-10, show line m of table-n.txt                |
| 24  | `24_url_word_count.py`            | Fetch URL, count words                                      |
| 25  | `25_gdp_eurostat.py`              | EU GDP per capita from Eurostat by country initials          |
| 26  | `26_phone_directory.py`          | Phone directory: create, consult, add, delete (phone_directory.txt) |
| 27  | `27_quotes_stats.py`              | Load quotes.csv to dict, create min/max/mean CSV             |
| 28  | `28_course_grades.py`             | Load grades, final grade, approved/suspended lists           |
| 29  | `29_course_grades_json.py`        | Same rules as 28 using `data/student_grades.json`            |
| 30  | `30_csv_full_operations.py`       | CSV practice: create, append, DictReader/DictWriter, update, delete (`students.csv`) |

## Data files

- `students.txt` - Used by 04 and 10 (created by 01_write or provided as seed)
- `students.csv` - Created by 30 (CSV full operations demo)
- `employees.json` - Created by 12_crud_employees
- `data/quotes.csv` - Stock quotes (27)
- `data/grades.csv` - Course grades (28)
- `table-n.txt` - Multiplication tables (21, 22, 23)
- `phone_directory.txt` - Phone directory (26)

## Suggested order

**Basic flow:** 01 → 02 → 03 → 04 → 05 → 09 → 10

**Full flow:** 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17 → 18 → 19 → 20

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

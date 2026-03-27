**contenido completo del PDF convertido a Markdown (.md)** sin omitir nada, fiel al original y bien estructurado.

---

```md id="lab2csvfull"
# Python for Data Science • Lab 2

---

# Lab 2 — CSV Manipulation with Python

**Course:** Python for Data Science  
**Estimated time:** 60–90 minutes  
**Files included:** lab2_students.csv  

---

## Overview

In this lab you will practice reading a CSV file, accessing values by column name, performing basic analysis, and printing useful summaries. Use the provided file lab2_students.csv as your dataset. :contentReference[oaicite:0]{index=0}

---

## Learning Objectives

- Import and use Python’s built-in csv module.
- Read a CSV file with csv.DictReader().
- Convert string values from a CSV file into numeric types when needed.
- Compute summary statistics from tabular data.
- Filter records and count repeated categories with a dictionary.

---

## Instructions

1. Download the file lab2_students.csv and save it in the same folder as your Python program.  
2. Create a Python file named lab2_csv_manipulation.py.  
3. Complete all tasks below in one program unless your instructor tells you otherwise.  
4. Add clear comments before each task.  
5. Submit your Python file and a screenshot of your output.  

---

## Dataset Preview

| Name    | Age | Major         | GPA |
|---------|-----|--------------|-----|
| Alice   | 20  | Computer Sci | 3.8 |
| Bob     | 22  | Math         | 3.2 |
| Charlie | 19  | Physics      | 3.6 |
| Diana   | 21  | Biology      | 3.9 |
| Ethan   | 23  | Computer Sci | 3.4 |

---

# Lab Tasks

---

## Task 1 — Import and open the file

- Import the csv module.  
- Open lab2_students.csv in read mode.  
- Create a DictReader object named reader.  

---

## Task 2 — Print all students in a clean format

- Loop through the CSV rows.  
- Print each student in this exact style:

```

Name: Alice | Age: 20 | Major: Computer Sci | GPA: 3.8

```

---

## Task 3 — Calculate the average age

- Compute the average age of all students in the file.  
- Print the result with a label such as:

```

Average age: 21.0

```

---

## Task 4 — Find the oldest student

- Determine which student has the highest age.  
- Print both the name and age of the oldest student.  

---

## Task 5 — Print only Computer Sci students

- Filter the data so that only students whose major is Computer Sci are printed.  
- Print only the names of those students.  

---

## Task 6 — Count how many students are in each major

- Use a dictionary to count the number of students in each major.  
- Print the final dictionary or print one line per major.  

---

## Task 7 — Print students with GPA 3.5 or higher

- Convert the GPA value to float.  
- Print the names of all students whose GPA is 3.5 or higher.  

---

# Stretch Challenge (Optional)

- Find the average GPA for the entire file.  
- Print all students older than 21.  
- Write a short summary of your results to a text file named lab2_summary.txt.  

---

# Grading Rubric

| Category | Points | What earns full credit |
|----------|--------|------------------------|
| Correct use of csv module and DictReader | 15 | Imports csv, opens the file correctly, and reads rows by column names. |
| Task 2: clean formatted output | 15 | All records print clearly and match the requested format. |
| Task 3: average age | 15 | Average is computed correctly using numeric conversion. |
| Task 4: oldest student | 15 | Program correctly identifies and prints the oldest student. |
| Task 5: filter by major | 10 | Only Computer Sci students are printed. |
| Task 6: count by major | 15 | Dictionary counting logic is correct and output is readable. |
| Task 7: GPA filter | 10 | Students with GPA 3.5 or higher are correctly printed. |
| Code quality and comments | 5 | Code is readable, organized, and includes helpful comments. |

---

# Total: 100 points

---

# Submission Checklist

- lab2_csv_manipulation.py  
- Screenshot of program output  
- Optional: lab2_summary.txt if you complete the stretch challenge  
```

---




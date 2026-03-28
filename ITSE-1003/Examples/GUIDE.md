# 🧑‍💻 Python Data Analysis + Databases — Beginner Guide (ITSE-1003)

---

# 🧠 0. What You Will Learn

By the end of this guide, you will know how to:

* Create a Python project
* Set up a virtual environment
* Install packages
* Run Python scripts
* Analyze data
* Connect Python to databases

---

# 📁 1. Create Your Project

Open your terminal and run:

```bash
mkdir python_lab_ex
cd python_lab_ex
```

👉 This creates your working folder.

---

# 🐍 2. Create a Virtual Environment (VERY IMPORTANT)

```bash
# Create environment
python -m venv .venv
```

---

## ▶️ Activate the environment

### 🪟 Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

### 🍎 Mac/Linux:

```bash
source .venv/bin/activate
```

---

# 📦 3. Install Required Packages

```bash
pip install numpy pandas matplotlib seaborn scipy scikit-learn openpyxl statsmodels
```

---

## 💾 Save dependencies

```bash
pip freeze > requirements.txt
```

---

# ▶️ 4. How to Run Python Scripts

```bash
python filename.py
```

or (Windows):

```bash
py filename.py
```

---

# 🧪 5. Verify Installation

Run Python:

```bash
python
```

Then test:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Everything works!")
```

---

# 📂 Sample data in this repository (`Examples/data/`)

At this point you already know how to **create a folder**, **activate the virtual environment**, and **run a script**. The next sections use **pandas** and **SQLite** with real files.

If you are working inside **`ITSE-1003/Examples`** from this repo, most sample CSVs and the practice database live in **`data/`** (next to **`classes/`**, **`file_handling/`**, and shared root scripts). Hospital demo CSV lives under **`hospital/data/`**; sales invoices and `sales.db` under **`sales/data/`**. If you are only using your own empty project (for example `python_lab_ex`), you can skip the table below until you add your own files—or copy these samples into a `data` folder you create yourself.

| File | Purpose |
| ---- | ------- |
| `exam_data.csv` | Student exams (scores, subjects, teachers) — used to build `school.db` |
| `people.csv` | People records (name, age, city, …) — used by `file_handling/run_csv_workshop.py`, `file_handling/csv_reading.py`, `file_handling/csv_people_analysis.py` |
| `hospital/data/hospital_data.csv` | Hospital / patient-style demo rows (`hospital/hospital_system.py`) |
| `vehicles.csv` | Vehicle demo rows |
| `school.db` | SQLite database (`users` + `exam_scores`) — **rebuild** with the script below |
| `generated/` | Optional outputs when you run `file_handling/run_csv_workshop.py` |

### Rebuild `school.db`

From the **`Examples`** folder:

```bash
python data/build_school_db.py
```

That recreates `data/school.db` from `data/exam_data.csv` (5 users, all exam rows).

### Paths with `pathlib` (recommended)

So your code always finds `data/` next to your script (no matter where you opened the terminal from):

```python
from pathlib import Path

EXAMPLES_DIR = Path(__file__).resolve().parent
DATA_DIR = EXAMPLES_DIR / "data"

exam_csv = DATA_DIR / "exam_data.csv"
db_path = DATA_DIR / "school.db"
```

---

# 📊 6. Essential Libraries for Data Analysis

---

## 🔹 NumPy — Numerical Computing

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr.mean())
```

---

## 🔹 Pandas — Data Analysis (MOST IMPORTANT)

```python
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"
df = pd.read_csv(DATA_DIR / "exam_data.csv")
print(df.head())
```

---

## 🔹 Matplotlib — Basic Visualization

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

---

## 🔹 Seaborn — Advanced Visualization

```python
import seaborn as sns

sns.histplot([1, 2, 2, 3, 3, 3])
```

---

## 🔹 Other Important Libraries

| Library      | Purpose              |
| ------------ | -------------------- |
| scipy        | Scientific computing |
| scikit-learn | Machine learning     |
| openpyxl     | Excel files          |
| statsmodels  | Advanced statistics  |

---

# 🚀 7. First Real Example

```python
# =========================================
# File: analysis.py
# Description: Basic data analysis
# =========================================

from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"
df = pd.read_csv(DATA_DIR / "exam_data.csv")

print(df.describe())

passed = df[df["Score"] > 80]
print(passed)
```

---

# 🧠 8. Working with Databases in Python

---

## 🔹 Concept

```
Python → Driver → Database
Python → ORM → Driver → Database
```

---

# 🟢 SQLite (No installation needed)

```python
from pathlib import Path
import sqlite3

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
db_path = DATA_DIR / "school.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()
conn.close()
```

> **Tip:** For the ready-made schema and sample rows, run `python data/build_school_db.py` from the `Examples` folder instead of creating tables by hand.

---

# 🐬 MySQL

```bash
pip install mysql-connector-python
```

```python
import mysql.connector
```

---

# 🐘 PostgreSQL

```bash
pip install psycopg2-binary
```

```python
import psycopg2
```

---

# 🧊 SQL Server

```bash
pip install pyodbc
```

```python
import pyodbc
```

---

# 🌐 SQLAlchemy (BEST PRACTICE)

```bash
pip install sqlalchemy
```

```python
from pathlib import Path
from sqlalchemy import create_engine

DATA_DIR = Path(__file__).resolve().parent / "data"
db_path = DATA_DIR / "school.db"
engine = create_engine(f"sqlite:///{db_path.resolve().as_posix()}")
```

---

# 🔗 9. Combine Data Analysis + Database

```python
# =========================================
# File: db_analysis.py
# =========================================

from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

DATA_DIR = Path(__file__).resolve().parent / "data"
db_path = DATA_DIR / "school.db"
engine = create_engine(f"sqlite:///{db_path.resolve().as_posix()}")

df = pd.read_sql("SELECT * FROM users", engine)
print(df.head())

scores = pd.read_sql(
    "SELECT student_name, subject, score FROM exam_scores WHERE score >= 85",
    engine,
)
print(scores.head())
```

---

# ⚙️ 10. Install Full Database Stack (Optional)

```bash
pip install sqlalchemy psycopg2-binary pymysql mysql-connector-python pyodbc
```

---

# 🔄 11. Update Python

## Check version:

```bash
python --version
```

---

## Windows (recommended):

```bash
winget upgrade Python.Python
```

---

# 🧱 12. Best Practices

✔ Always use virtual environments
✔ Save dependencies (`requirements.txt`)
✔ Use `pandas + numpy` as core tools
✔ Learn SQL + Python together

---

# 🧠 13. Professional Stack

| Purpose       | Tool                 |
| ------------- | -------------------- |
| Data analysis | pandas + numpy       |
| Visualization | matplotlib + seaborn |
| Database      | SQLAlchemy           |
| Backend DB    | PostgreSQL           |

---

# 🎓 Final Thought

> You are no longer just writing code—you are building **data systems**.

---

# 🔥 Practice Challenge

1. Create a project
2. Install libraries
3. Load a CSV
4. Filter data
5. Save results to Excel
6. Store data in SQLite

---


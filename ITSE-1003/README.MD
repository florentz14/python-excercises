# ITSE-1003

Course materials: labs, examples, and mini projects for **ITSE-1003** (Python, OOP, CSV, SQLite, SQLAlchemy).

## Structure

```text
ITSE-1003/
├── README.MD                 ← This file (course overview)
├── Examples/                 ← Main lab folder (see Examples/README.md)
│   ├── data/                 ← Shared CSVs, school.db, build_school_db.py
│   ├── sales/                ← Sales / invoicing (SQLAlchemy, gestion_ventas.py)
│   ├── employees/            ← Employee OOP demo + menu
│   ├── customers/            ← Customer form + CRUD (utils)
│   ├── hospital/             ← Hospital OOP demo; models/ + data/hospital_data.csv
│   ├── examples_paths.py     ← Central path constants
│   ├── utils.py              ← Shared input validation helpers
│   ├── GUIDE.md              ← Setup: venv, pip, pandas, SQLite, paths
│   └── …                     ← Standalone topic scripts (POO, CSV workshop, etc.)
└── M2-FBAEZ/
    ├── README.md
    └── pet_management_system.py
```

## Modules

| Folder | Description |
| ------ | ----------- |
| **[`Examples/`](Examples/README.md)** | Course examples: OOP sequences, CSV workshop, `database_config` / `.env`, domain mini-apps in **`sales/`**, **`employees/`**, **`customers/`**, **`hospital/`**. |
| **`M2-FBAEZ/`** | Separate mini project: Pet Management System (OOP). |

Full index, tables, and `sys.path` notes: **[`Examples/README.md`](Examples/README.md)**.

## How to run

Use **Python 3** from the repo root or from **`ITSE-1003/Examples`** (many scripts expect `cd` into `Examples`).

```bash
# Examples — CSV workshop
cd ITSE-1003/Examples
python run_csv_workshop.py

# Examples — domain folders (from Examples/)
python sales/gestion_ventas.py
python employees/employee_menu.py
python customers/customer_form.py
python hospital/hospital_system.py

# M2-FBAEZ — from repo root
python ITSE-1003/M2-FBAEZ/pet_management_system.py
```

Install extras as needed (e.g. `tabulate`, `python-dotenv`, `sqlalchemy`); see the repo **[`requirements.txt`](../requirements.txt)**.

## Author

- Florentino Baez

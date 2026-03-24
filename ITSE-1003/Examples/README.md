<!--
-------------------------------------------------
File Name: ITSE-1003/Examples/README.md
Author: Florentino Báez
Date: 3/20/2026
Description: Index for ITSE-1003 Examples (OOP, CSV, data, DB, extras).
-------------------------------------------------
-->

# ITSE-1003 — `Examples/`

Material de apoyo y laboratorios: **POO en Python**, **CSV**, **datos de ejemplo**, **SQLite** y scripts sueltos. Todo está pensado para ejecutarse con el intérprete de Python 3 desde la carpeta **`Examples/`** o desde la **raíz del repo** (salvo donde se indique).

**Curso (carpeta padre):** ver [`../README.MD`](../README.MD). Proyecto aparte: [`../M2-FBAEZ/`](../M2-FBAEZ/) (sistema de mascotas).

---

## Guía principal

| Recurso | Contenido |
| ------- | --------- |
| **`GUIDE.md`** | Entorno virtual, `pip`, pandas, `pathlib`, SQLite, SQLAlchemy; rutas hacia **`data/`**. |

---

## Configuración y base de datos

| Archivo | Uso |
| ------- | --- |
| **`examples_paths.py`** | Rutas a `data/`, `data/generated/`, CSVs y `school.db` (el nombre evita choque con `settings.py` de la raíz del repo). |
| **`database_config.py`** | Carga **`Examples/.env`** con **`python-dotenv`** (`load_dotenv`), luego lee variables para la cadena de conexión (SQLite por defecto → `data/school.db`). Ejecutar: `python database_config.py`. |
| **`.env.example`** | Plantilla (versionar en git). Copia a **`.env`** en la misma carpeta que `database_config.py` y ajusta valores. En la **raíz del repo**, [`.gitignore`](../../.gitignore) ignora `.env` y variantes (`.env.*`) pero **no** ignora `.env.example`. |

Requisito para este módulo: `pip install python-dotenv` (también en [`requirements.txt`](../../requirements.txt) del repo).

---

## Datos y taller CSV

| Recurso | Uso |
| ------- | --- |
| **`data/`** | CSVs (`people.csv`, `exam_data.csv`, `vehicles.csv`), `school.db`, **`build_school_db.py`**. `hospital_data.csv` está en **`hospital/data/`**; facturas y `sales.db` en **`sales/data/`**. |
| **`run_csv_workshop.py`** | Recorre todo el taller CSV (lectura → escritura → análisis → formatos). |
| **`csv_reading.py`** / **`csv_writing.py`** / **`csv_people_analysis.py`** | Partes del taller por separado. |
| **`csv_examples.py`** | Alias que ejecuta `run_csv_workshop`. |
| **`data_preview.py`** | Vista rápida de CSVs + tablas SQLite (solo biblioteca estándar + `examples_paths`). |

Regenerar la base escolar:

```bash
cd ITSE-1003/Examples
python data/build_school_db.py
```

### Quién usa qué en `data/`

| Archivo | Usado por |
| ------- | --------- |
| `people.csv` | `run_csv_workshop.py`, `csv_people_analysis.py`, `csv_reading.py`, `data_preview.py` |
| `exam_data.csv` | `data/build_school_db.py`, `data_preview.py`, ejemplos en **`GUIDE.md`** |
| `hospital/data/hospital_data.csv` | `hospital/hospital_system.py`, `data_preview.py` |
| `vehicles.csv` | `vehicle_class.py`, `data_preview.py` |
| `sales/data/invoices.csv` | `sales/invoice_model.py`, `data_preview.py` |
| `sales/data/invoice_lines.csv` | `sales/invoice_model.py`, `data_preview.py` |
| `school.db` | `database_config.py`, `data_preview.py`, **`GUIDE.md`** |
| `sales/data/sales.db` | `sales/gestion_ventas.py`, `sales/sales_database.py`, `data_preview.py` (se crea al ejecutar el menú) |
| `generated/` | Salida del taller CSV (ignorada por git salvo `.gitkeep`) |

### Gestión de ventas (SQLAlchemy + SQLite)

Carpeta **`sales/`**. Mini sistema en consola: clientes, suplidores, artículos, inventario, facturas en **borrador** / **finalizada** / **pagada** (al finalizar se descuenta existencia).

| Archivo | Rol |
| ------- | --- |
| `sales/sales_models.py` | Modelos ORM (`Supplier`, `Customer`, `Product`, `Inventory`, `Invoice`, `InvoiceLine`). |
| `sales/sales_database.py` | Motor SQLite (`sales/data/sales.db`), sesión, `init_db`, datos demo, `finalize_invoice`, `mark_invoice_paid`. |
| `sales/gestion_ventas.py` | Menú interactivo. Opción **99**: reiniciar BD y volver a cargar demo. |

```bash
cd ITSE-1003/Examples
python sales/gestion_ventas.py
```

Requiere **SQLAlchemy** (ver [`requirements.txt`](../../requirements.txt)).

### Gestión de empleados (POO + `utils`)

Carpeta **`employees/`**: modelo, gestor en memoria y menú interactivo (usa **`utils`** en `Examples/`).

| Archivo | Rol |
| ------- | --- |
| `employees/employee_model.py` | Clase `Employee`. |
| `employees/employee_manager.py` | `EmployeesManager` (importa `employee_model`). |
| `employees/employee_menu.py` | Menú interactivo (importa `employee_manager`). |

```bash
cd ITSE-1003/Examples
python employees/employee_menu.py
```

### Clientes (formulario + CRUD + `utils`)

Carpeta **`customers/`**: ejemplos con validaciones desde **`utils`** en `Examples/`.

| Archivo | Rol |
| ------- | --- |
| `customers/customer_form.py` | Clase `Customer` y formulario con entradas validadas. |
| `customers/customer_crud.py` | CRUD interactivo en memoria con las mismas utilidades. |

```bash
cd ITSE-1003/Examples
python customers/customer_form.py
python customers/customer_crud.py
```

### Sistema hospitalario (OOP + CSV)

Carpeta **`hospital/`**: demo con pacientes, doctores, citas y expedientes; carga **`hospital/data/hospital_data.csv`** vía `examples_paths`.

| Recurso | Rol |
| ------- | --- |
| `hospital/models/` | Modelos: `enums`, `person`, `patient`, `staff`, `doctor`, `nurse`, `appointment` (exportados en `models/__init__.py`). |
| `hospital/hospital_system.py` | Carga CSV, helpers y demo en `main` (importa `models`). |

```bash
cd ITSE-1003/Examples
python hospital/hospital_system.py
```

---

## POO — ejemplos por tema (orden sugerido)

Los nombres son **solo descriptivos** (sin prefijo `oop_01`, etc.). No dependen de `data/` salvo los que importan `utils` (indicados en la tabla de *sys.path* más abajo).

| # | Archivo | Tema |
| -: | ------- | ---- |
| 1 | `classes_objects.py` | Clases y objetos |
| 2 | `temperature_methods.py` | Métodos de instancia, de clase y estáticos |
| 3 | `bank_property.py` | Encapsulación con `@property` |
| 4 | `inheritance_animals.py` | Herencia y `super()` |
| 5 | `diamond_mro.py` | Herencia múltiple y MRO |
| 6 | `polymorphism_speak.py` | Polimorfismo y duck typing |
| 7 | `vehicles_override.py` | Sobrescritura de métodos |
| 8 | `abstract_shapes.py` | Clases abstractas (`ABC`) |
| 9 | `product_dunder.py` | Métodos mágicos / dunder |
| 10 | `nested_classes.py` | Clases internas |
| 11 | `class_instance_attrs.py` | Atributos de clase vs instancia |
| 12 | `car_composition.py` | Composición (HAS-A) |
| 13 | `employees/employee_model.py` | Modelo de empleado |
| 14 | `employees/employee_manager.py` | Gestor (importa `employee_model`) |
| 15 | `employees/employee_menu.py` | Menú interactivo (importa `employee_manager`) |
| 16 | `microwave_oop.py` | Estado con microondas |
| 17 | `book_dataclass.py` | `@dataclass` |
| 18 | `student_courses.py` | Agregación (estudiantes y cursos) |
| 19 | `logger_mixin.py` | Mixins |
| 20 | `traffic_enum.py` | `Enum` y estado del objeto |
| 21 | `file_context_manager.py` | Context manager (`__enter__` / `__exit__`) |
| 22 | `payment_strategy.py` | Estrategia con `Protocol` |
| 23 | `customers/customer_form.py` | Formulario + validaciones de `utils` |
| 24 | `customers/customer_crud.py` | CRUD interactivo + `utils` |

### Otros ejemplos POO / clases (fuera de la secuencia 1–24)

| Archivo | Notas |
| ------- | ----- |
| `car_class.py` | Clase `Car` ilustrativa |
| `tv_class.py` | Clase `TV` ilustrativa |
| `user_class.py` | Usuario con getter/setter de email |
| `person_age.py` | Edad y fechas con `utils` |
| `hospital/hospital_system.py` | Sistema hospitalario; carga `hospital/data/hospital_data.csv` |
| `vehicle_class.py` | Herencia vehículos; carga `data/vehicles.csv` |
| `sales/invoice_model.py` | Factura maestra + líneas de detalle; carga `sales/data/invoices.csv` y `invoice_lines.csv` |

---

## Cómo ejecutar

Desde la **raíz del repositorio**:

```bash
python ITSE-1003/Examples/classes_objects.py
```

Desde **`ITSE-1003/Examples`**:

```bash
python classes_objects.py
python run_csv_workshop.py
```

### `sys.path` (imports locales)

Estos archivos añaden la carpeta `Examples/` a `sys.path` para que funcionen `utils` e imports entre módulos aunque ejecutes desde la raíz del repo:

- `customers/customer_form.py`, `customers/customer_crud.py`, `employees/employee_manager.py`, `employees/employee_menu.py`, `hospital/hospital_system.py`, `sales/invoice_model.py`

---

## Dependencias frecuentes

Instala según lo que ejecutes:

- **`tabulate`** — tablas en consola (CSV workshop, varios ejemplos).
- **`python-dotenv`** — necesario para `database_config.py` (carga `.env`).
- Para seguir **`GUIDE.md`**: `pandas`, `numpy`, `matplotlib`, `sqlalchemy`, etc., según la sección.

```bash
pip install tabulate
```

---

## `utils.py`

Funciones compartidas (entradas validadas, fechas, email, etc.) usadas por **`customers/customer_form.py`**, **`customers/customer_crud.py`**, **`employees/employee_manager.py`**, **`person_age.py`**, y otros.

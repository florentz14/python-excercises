## <!--

File Name: ITSE-1003/Examples/README.md
Author: Florentino Báez
Date: 3/20/2026
Description: Index for ITSE-1003 Examples (OOP, CSV, data, DB, extras).

---

-->

# ITSE-1003 — `Examples/`

Material de apoyo y laboratorios: **POO en Python**, **CSV**, **datos de ejemplo**, **SQLite** y scripts sueltos. Todo está pensado para ejecutarse con el intérprete de Python 3 desde la carpeta **`Examples/`** o desde la **raíz del repo** (salvo donde se indique).

**Layout (English folder names):** standalone **OOP** scripts live under **`classes/`**; **CSV and file I/O** demos under **`file_handling/`**. Shared modules (**`utils.py`**, **`examples_paths.py`**, **`database_config.py`**, **`users_crud.py`**) stay at the **`Examples/`** root. Mini-projects remain in **`hospital/`**, **`sales/`**, **`employees/`**, **`customers/`**.

**Curso (carpeta padre):** ver [`../README.MD`](../README.MD). Proyecto aparte: [`../M2-FBAEZ/`](../M2-FBAEZ/) (sistema de mascotas).

---

## Guía principal

| Recurso        | Contenido                                                                               |
| -------------- | --------------------------------------------------------------------------------------- |
| **`GUIDE.md`** | Entorno virtual, `pip`, pandas, `pathlib`, SQLite, SQLAlchemy; rutas hacia **`data/`**. |

---

## Configuración y base de datos

| Archivo                  | Uso                                                                                                                                                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`examples_paths.py`**  | Rutas a `data/`, `data/generated/`, CSVs y `school.db` (el nombre evita choque con `settings.py` de la raíz del repo).                                                                                                                            |
| **`database_config.py`** | Carga **`Examples/.env`** con **`python-dotenv`** (`load_dotenv`), luego lee variables para la cadena de conexión (SQLite por defecto → `data/school.db`). Ejecutar: `python database_config.py`.                                                 |
| **`.env.example`**       | Plantilla (versionar en git). Copia a **`.env`** en la misma carpeta que `database_config.py` y ajusta valores. En la **raíz del repo**, [`.gitignore`](../../.gitignore) ignora `.env` y variantes (`.env.*`) pero **no** ignora `.env.example`. |

Requisito para este módulo: `pip install python-dotenv` (también en [`requirements.txt`](../../requirements.txt) del repo).

---

## Datos y taller CSV

Carpeta **`file_handling/`** (lectura/escritura CSV, vista previa de datos, context manager de archivo).

| Recurso                                                                                                              | Uso                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`data/`**                                                                                                          | CSVs (`people.csv`, `exam_data.csv`, `vehicles.csv`), `school.db`, **`build_school_db.py`**. `hospital_data.csv` está en **`hospital/data/`**; facturas y `sales.db` en **`sales/data/`**. |
| **`file_handling/run_csv_workshop.py`**                                                                              | Recorre todo el taller CSV (lectura → escritura → análisis → formatos).                                                                                                                    |
| **`file_handling/csv_reading.py`** / **`file_handling/csv_writing.py`** / **`file_handling/csv_people_analysis.py`** | Partes del taller por separado.                                                                                                                                                            |
| **`file_handling/csv_examples.py`**                                                                                  | Alias que ejecuta `run_csv_workshop`.                                                                                                                                                      |
| **`file_handling/data_preview.py`**                                                                                  | Vista rápida de CSVs + tablas SQLite (solo biblioteca estándar + `examples_paths`).                                                                                                        |
| **`file_handling/file_context_manager.py`**                                                                          | Context manager que escribe un archivo de nota bajo **`Examples/`**.                                                                                                                       |

Regenerar la base escolar:

```bash
cd ITSE-1003/Examples
python data/build_school_db.py
```

### Quién usa qué en `data/`

| Archivo                           | Usado por                                                                                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `people.csv`                      | `file_handling/run_csv_workshop.py`, `file_handling/csv_people_analysis.py`, `file_handling/csv_reading.py`, `file_handling/data_preview.py` |
| `exam_data.csv`                   | `data/build_school_db.py`, `file_handling/data_preview.py`, ejemplos en **`GUIDE.md`**                                                       |
| `hospital/data/hospital_data.csv` | `hospital/hospital_system.py`, `file_handling/data_preview.py`                                                                               |
| `vehicles.csv`                    | `classes/vehicle_class.py`, `file_handling/data_preview.py`                                                                                  |
| `sales/data/invoices.csv`         | `sales/invoice_model.py`, `file_handling/data_preview.py`                                                                                    |
| `sales/data/invoice_lines.csv`    | `sales/invoice_model.py`, `file_handling/data_preview.py`                                                                                    |
| `school.db`                       | `database_config.py`, `file_handling/data_preview.py`, **`GUIDE.md`**                                                                        |
| `sales/data/sales.db`             | `sales/gestion_ventas.py`, `sales/sales_database.py`, `file_handling/data_preview.py` (se crea al ejecutar el menú)                          |
| `generated/`                      | Salida del taller CSV (ignorada por git salvo `.gitkeep`)                                                                                    |

### Gestión de ventas (SQLAlchemy + SQLite)

Carpeta **`sales/`**. Mini sistema en consola: clientes, suplidores, artículos, inventario, facturas en **borrador** / **finalizada** / **pagada** (al finalizar se descuenta existencia).

| Archivo                   | Rol                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `sales/sales_models.py`   | Modelos ORM (`Supplier`, `Customer`, `Product`, `Inventory`, `Invoice`, `InvoiceLine`).                       |
| `sales/sales_database.py` | Motor SQLite (`sales/data/sales.db`), sesión, `init_db`, datos demo, `finalize_invoice`, `mark_invoice_paid`. |
| `sales/gestion_ventas.py` | Menú interactivo. Opción **99**: reiniciar BD y volver a cargar demo.                                         |

```bash
cd ITSE-1003/Examples
python sales/gestion_ventas.py
```

Requiere **SQLAlchemy** (ver [`requirements.txt`](../../requirements.txt)).

### Gestión de empleados (POO + `utils`)

Carpeta **`employees/`**: modelo, gestor en memoria y menú interactivo (usa **`utils`** en `Examples/`).

| Archivo                         | Rol                                            |
| ------------------------------- | ---------------------------------------------- |
| `employees/employee_model.py`   | Clase `Employee`.                              |
| `employees/employee_manager.py` | `EmployeesManager` (importa `employee_model`). |
| `employees/employee_menu.py`    | Menú interactivo (importa `employee_manager`). |

```bash
cd ITSE-1003/Examples
python employees/employee_menu.py
```

### Clientes (formulario + CRUD + `utils`)

Carpeta **`customers/`**: ejemplos con validaciones desde **`utils`** en `Examples/`.

| Archivo                      | Rol                                                    |
| ---------------------------- | ------------------------------------------------------ |
| `customers/customer_form.py` | Clase `Customer` y formulario con entradas validadas.  |
| `customers/customer_crud.py` | CRUD interactivo en memoria con las mismas utilidades. |

```bash
cd ITSE-1003/Examples
python customers/customer_form.py
python customers/customer_crud.py
```

### Sistema hospitalario (OOP + CSV)

Carpeta **`hospital/`**: demo con pacientes, doctores, citas y expedientes; carga **`hospital/data/hospital_data.csv`** vía `examples_paths`.

| Recurso                       | Rol                                                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `hospital/models/`            | Modelos: `enums`, `person`, `patient`, `staff`, `doctor`, `nurse`, `appointment` (exportados en `models/__init__.py`). |
| `hospital/hospital_system.py` | Carga CSV, helpers y demo en `main` (importa `models`).                                                                |

```bash
cd ITSE-1003/Examples
python hospital/hospital_system.py
```

---

## POO — ejemplos por tema (orden sugerido)

Carpeta **`classes/`** (objetos, herencia, polimorfismo, etc.). Los nombres son **solo descriptivos** (sin prefijo `oop_01`, etc.). No dependen de `data/` salvo los que importan `examples_paths` o `utils` (ver _sys.path_ más abajo).

|   # | Archivo                           | Tema                                          |
| --: | --------------------------------- | --------------------------------------------- |
|   1 | `classes/classes_objects.py`      | Clases y objetos                              |
|   2 | `classes/temperature_methods.py`  | Métodos de instancia, de clase y estáticos    |
|   3 | `classes/bank_property.py`        | Encapsulación con `@property`                 |
|   4 | `classes/inheritance_animals.py`  | Herencia y `super()`                          |
|   5 | `classes/diamond_mro.py`          | Herencia múltiple y MRO                       |
|   6 | `classes/polymorphism_speak.py`   | Polimorfismo y duck typing                    |
|   7 | `classes/vehicles_override.py`    | Sobrescritura de métodos                      |
|   8 | `classes/abstract_shapes.py`      | Clases abstractas (`ABC`)                     |
|   9 | `classes/product_dunder.py`       | Métodos mágicos / dunder                      |
|  10 | `classes/nested_classes.py`       | Clases internas                               |
|  11 | `classes/class_instance_attrs.py` | Atributos de clase vs instancia               |
|  12 | `classes/car_composition.py`      | Composición (HAS-A)                           |
|  13 | `employees/employee_model.py`     | Modelo de empleado                            |
|  14 | `employees/employee_manager.py`   | Gestor (importa `employee_model`)             |
|  15 | `employees/employee_menu.py`      | Menú interactivo (importa `employee_manager`) |
|  16 | `classes/microwave_oop.py`        | Estado con microondas                         |
|  17 | `classes/book_dataclass.py`       | `@dataclass`                                  |
|  18 | `classes/student_courses.py`      | Agregación (estudiantes y cursos)             |
|  19 | `classes/logger_mixin.py`         | Mixins                                        |
|  20 | `classes/traffic_enum.py`         | `Enum` y estado del objeto                    |
|  21 | `classes/payment_strategy.py`     | Estrategia con `Protocol`                     |
|  22 | `customers/customer_form.py`      | Formulario + validaciones de `utils`          |
|  23 | `customers/customer_crud.py`      | CRUD interactivo + `utils`                    |

_Context manager de archivo:_ ver **`file_handling/file_context_manager.py`** (taller de archivos).

### Otros ejemplos POO / clases (fuera de la secuencia)

| Archivo                            | Notas                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------ |
| `classes/car_class.py`             | Clase `Car` ilustrativa                                                                    |
| `classes/tv_class.py`              | Clase `TV` ilustrativa                                                                     |
| `classes/user_class.py`            | Usuario con getter/setter de email                                                         |
| `classes/person_age.py`            | Edad y fechas con `utils`                                                                  |
| `classes/person.py`                | Modelo Pydantic (persona)                                                                  |
| `classes/cls_*.py`, `cls_buggy.py` | Vehículos, herencia, cuenta bancaria con errores didácticos                                |
| `hospital/hospital_system.py`      | Sistema hospitalario; carga `hospital/data/hospital_data.csv`                              |
| `classes/vehicle_class.py`         | Herencia vehículos; carga `data/vehicles.csv`                                              |
| `sales/invoice_model.py`           | Factura maestra + líneas de detalle; carga `sales/data/invoices.csv` y `invoice_lines.csv` |

---

## Cómo ejecutar

Desde la **raíz del repositorio**:

```bash
python ITSE-1003/Examples/classes/classes_objects.py
python ITSE-1003/Examples/file_handling/run_csv_workshop.py
```

Desde **`ITSE-1003/Examples`**:

```bash
python classes/classes_objects.py
python file_handling/run_csv_workshop.py
```

---

## Instalación y Uso de Jupyter y JupyterLab

Jupyter Notebook y JupyterLab son entornos interactivos para ejecutar código Python, crear notebooks con celdas de código, texto y visualizaciones. Son útiles para análisis de datos, prototipado y enseñanza.

### Instalación desde la CLI

Jupyter y JupyterLab están incluidos en el [`requirements.txt`](../../requirements.txt) del repositorio. Para instalarlos:

1. **Activar el entorno virtual** (desde la raíz del repo):

   ```bash
   # En Windows (PowerShell)
   & .\.venv\Scripts\Activate.ps1

   # En Linux/Mac
   source .venv/bin/activate
   ```

2. **Instalar dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

   Esto instala `jupyter>=1.0.0` y `jupyterlab>=4.0.0`.

Si prefieres instalar manualmente:

```bash
pip install jupyter jupyterlab
```

### Inicialización y Configuración

1. **Verificar instalación**:

   ```bash
   jupyter --version
   jupyterlab --version
   ```

2. **Generar configuración (opcional)**:

   ```bash
   jupyter notebook --generate-config
   ```

   Esto crea `~/.jupyter/jupyter_notebook_config.py` para personalizar (puertos, contraseñas, etc.).

3. **Configurar contraseña (opcional, para acceso remoto)**:
   ```bash
   jupyter notebook password
   ```
   Ingresa una contraseña segura.

### Ejecutar Jupyter Notebook

- **Desde la CLI**:

  ```bash
  jupyter notebook
  ```

  Se abre en el navegador en `http://localhost:8888` (o el puerto configurado).

- **Especificar directorio**:

  ```bash
  jupyter notebook --notebook-dir=ITSE-1003/Examples
  ```

- **Con puerto específico**:
  ```bash
  jupyter notebook --port=9999
  ```

### Ejecutar JupyterLab

- **Desde la CLI**:

  ```bash
  jupyter lab
  ```

  Se abre en el navegador en `http://localhost:8888/lab` (interfaz más moderna que Notebook).

- **Especificar directorio y puerto**:
  ```bash
  jupyter lab --notebook-dir=ITSE-1003/Examples --port=9999
  ```

### Comandos Útiles

- **Listar kernels disponibles**:

  ```bash
  jupyter kernelspec list
  ```

- **Instalar kernel para el entorno virtual** (si no aparece):

  ```bash
  pip install ipykernel
  python -m ipykernel install --user --name=myenv
  ```

- **Convertir notebook a script**:

  ```bash
  jupyter nbconvert --to script notebook.ipynb
  ```

- **Ejecutar notebook desde CLI**:
  ```bash
  jupyter nbconvert --execute notebook.ipynb
  ```

### Notas

- **Entorno virtual**: Asegúrate de activar el entorno antes de ejecutar Jupyter para que use las dependencias correctas.
- **Archivos .ipynb**: Los notebooks se guardan como JSON. Puedes abrirlos en VS Code con la extensión de Jupyter.
- **Extensiones**: Para más funcionalidades, instala extensiones como `jupyter_contrib_nbextensions`.
- **Problemas comunes**: Si el navegador no se abre, copia la URL de la terminal. Para acceso remoto, configura `--ip=0.0.0.0` y un token.

Para más información, consulta la [documentación oficial de Jupyter](https://jupyter.org/documentation).

---

### `sys.path` (imports locales)

Estos archivos añaden la carpeta `Examples/` (y cuando hace falta `file_handling/`) a `sys.path` para que funcionen `utils`, `examples_paths` e imports entre módulos aunque ejecutes desde la raíz del repo:

- `file_handling/csv_reading.py`, `file_handling/csv_writing.py`, `file_handling/csv_people_analysis.py`, `file_handling/data_preview.py`, `file_handling/run_csv_workshop.py`, `file_handling/csv_examples.py`
- `classes/vehicle_class.py`, `classes/user_class.py`, `classes/person_age.py`
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

Funciones compartidas (entradas validadas, fechas, email, etc.) usadas por **`customers/customer_form.py`**, **`customers/customer_crud.py`**, **`employees/employee_manager.py`**, **`classes/person_age.py`**, **`file_handling/csv_reading.py`**, y otros.

# School Management API

API REST con **FastAPI**, **SQLAlchemy 2** y **MySQL** para gestionar estudiantes, instructores, cursos e inscripciones. El esquema de datos está alineado con `../data/school_db.sql` del repositorio de ejemplos.

La lógica de negocio vive en `services/` y las rutas HTTP en `routers/`, siguiendo el mismo enfoque que el ejemplo `music_api`.

## Requisitos

- Python 3.10 o superior (recomendado 3.12+)
- MySQL 8 con la base `school_db` creada y las tablas cargadas (puedes usar el script SQL mencionado arriba)

## Instalación

```bash
cd ITSE-1003/Examples/school_app
python -m venv .venv
```

En Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copia las variables de entorno y ajusta usuario, contraseña y host:

```bash
copy .env.example .env
```

Al menos define **`DATABASE_URL`**, por ejemplo:

```text
DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/school_db
```

## Ejecutar la API

Desde la carpeta `school_app`:

```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

- Documentación interactiva: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Raíz: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (lista enlaces a los recursos)

## Estructura del proyecto

| Ruta | Contenido |
|------|-----------|
| `main.py` | App FastAPI, CORS, `lifespan` (creación de tablas al arrancar), registro de routers |
| `database.py` | Motor SQLAlchemy, sesiones, `get_db`, utilidades de conexión |
| `models/` | Modelos ORM (`Student`, `Instructor`, `Course`, `Enrollment`) |
| `schemas/` | Esquemas Pydantic (entrada/salida de la API) |
| `services/` | Reglas de negocio (soft delete, emails únicos, validaciones de inscripción) |
| `routers/` | Endpoints HTTP por recurso |

## Endpoints principales

| Prefijo | Descripción |
|---------|-------------|
| `GET/POST /students/` | Lista (paginación, `search` opcional) y alta |
| `GET/PUT/DELETE /students/{id}` | Detalle, actualización y baja lógica |
| `GET/POST /instructors/` | Igual para instructores (`search` opcional) |
| `GET/POST /courses/` | Cursos; lista admite `search` y `instructor_id` |
| `GET/POST /enrollments/` | Inscripciones; lista admite `student_id` y/o `course_id` |

Las respuestas de creación usan código **201 Created**. Los borrados son **soft delete** (`deleted_at`); no se eliminan filas de la base de datos.

### Comportamiento destacado

- **Estudiantes e instructores**: email único en base de datos; la API responde **409** si el email ya está en uso.
- **Cursos**: si se indica `instructor_id`, debe existir un instructor activo (no borrado lógicamente).
- **Inscripciones**: no se permiten duplicados activos para la misma pareja estudiante-curso. Si existía una inscripción en soft delete, un nuevo alta **reactiva** esa fila en lugar de insertar otra (respeta la restricción `UNIQUE` de MySQL).

## Probar la conexión a MySQL

```bash
python database.py
```

Ejecuta la función `test_connection()` e imprime si la conexión fue correcta.

## Desarrollo

Dependencias de prueba HTTP opcionales: `pytest`, `httpx` (ver `requirements.txt`).

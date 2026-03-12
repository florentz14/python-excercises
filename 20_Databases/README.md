# 20_Databases

Conexión y operaciones con bases de datos usando Python (MySQL/MariaDB, SQLite3, PostgreSQL y MongoDB).

## Configuración

1. Crear archivo `.env` en la raíz del proyecto con:
   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=tu_password
   MYSQL_DATABASE=ATM_Database_Schema  
   MYSQL_PORT=3306

   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   POSTGRES_DB=books_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=tu_password

   MONGO_URI=mongodb://localhost:27017
   MONGO_DB=books_db
   ```

2. Instalar dependencias:
   ```bash
   pip install mysql-connector-python psycopg2-binary pymongo python-dotenv bcrypt
   ```

## Archivos

| Archivo | Contenido |
|---------|-----------|
| `Tests/01_mysql_connection.py` | Prueba de conexión a MySQL/MariaDB |
| `02_atm_mysql_app.py` | Sistema ATM completo con base de datos |
| `03_atm_user_tool.py` | Herramienta para crear/listar/eliminar usuarios ATM |
| `04_books_sqlite.py` | Flujo CRUD completo con SQLite3 en archivo local |
| `05_books_postgres.py` | Flujo CRUD completo con PostgreSQL y transacciones |
| `06_books_sqlalchemy.py` | Flujo CRUD completo vía Pandas + SQLAlchemy |
| `07_books_mongo.py` | Flujo CRUD completo con MongoDB y agregaciones |
| `08_family_budget_loader.py` | Carga `Script_Sql/family_budget_complete.sql` y audita tablas vacías |
| `09_tasks_sqlite.py` | SQLite3 para gestión de tareas por proyecto (extendido) |
| `Script_Sql/` | Carpeta para scripts SQL |
| `Script_Sql/family_budget_complete.sql` | Script completo para recrear la base de presupuesto familiar |
| `Script_Sql/family_budget_seed_inserts.sql` | Inserts complementarios para tablas vacías del presupuesto familiar |

## Data Folder

- All generated SQLite databases are stored in `20_Databases/Data/`.
- CSV exports from the project/task manager are stored in `20_Databases/Data/reports/`.

## Sistema ATM con Base de Datos

### Características
- Autenticación de usuarios con contraseñas hasheadas (bcrypt)
- Depósitos y retiros con validación de fondos
- Historial completo de transacciones
- Exportación de historial a archivo de texto
- Registro de sesiones y auditoría
- Procedimientos almacenados para operaciones

### Tablas de la Base de Datos

| Tabla | Descripción |
|-------|-------------|
| `atm_users` | Usuarios del sistema |
| `atm_sessions` | Sesiones de usuario |
| `atm_transactions` | Depósitos y retiros |
| `atm_balance_snapshots` | Historial de balances |
| `atm_login_attempts` | Intentos de login |
| `atm_activity_log` | Log de actividades |
| `atm_history_exports` | Exportaciones realizadas |

### Instalación del Schema

```bash
# Crear la base de datos
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS ATM_Database_Schema;"

# Importar el schema
mysql -u root -p ATM_Database_Schema < <path_to_schema.sql>
```

### Usuarios de Prueba

| Username | Password | Balance Inicial |
|----------|----------|-----------------|
| test_user | 1234 | $0.00 |
| florentino | 1234 | $1,000.00 |

### Uso

```bash
# Probar conexión
python 20_Databases/Tests/01_mysql_connection.py

# Ejecutar sistema ATM
python 20_Databases/02_atm_mysql_app.py

# Gestionar usuarios (crear/listar/eliminar)
python 20_Databases/03_atm_user_tool.py

# Ejecutar ejemplo SQLite3
python 20_Databases/04_books_sqlite.py

# Ejecutar ejemplo PostgreSQL
python 20_Databases/05_books_postgres.py

# Ejecutar ejemplo MongoDB
python 20_Databases/07_books_mongo.py

# Auditar tablas vacías (sin ejecutar SQL)
python 20_Databases/08_family_budget_loader.py

# Ejecutar SQL y luego auditar tablas
python 20_Databases/08_family_budget_loader.py --apply

# Crear y poblar SQLite3 de gestión de proyectos/tareas
python 20_Databases/09_tasks_sqlite.py
```

### Menú del ATM

```
1 - Deposit
2 - Withdraw
3 - Check Balance
4 - Deposit History
5 - Withdrawal History
6 - Balance History
7 - Export History to File
8 - Exit
```

## Requisitos

- MySQL Server o MariaDB instalado y ejecutándose
- Base de datos `ATM_Database_Schema` creada
- Credenciales configuradas en `.env`
- Python 3.10+

## Dependencias

```
mysql-connector-python>=8.0.0
python-dotenv>=1.0.0
bcrypt>=4.0.0
```

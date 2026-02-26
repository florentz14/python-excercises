# 20_MySQL

Conexión y operaciones con bases de datos MySQL/MariaDB usando Python.

## Configuración

1. Crear archivo `.env` en la raíz del proyecto con:
   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=tu_password
   MYSQL_DATABASE=ATM_Database_Schema  
   MYSQL_PORT=3306
   ```

2. Instalar dependencias:
   ```bash
   pip install mysql-connector-python python-dotenv bcrypt
   ```

## Archivos

| Archivo | Contenido |
|---------|-----------|
| `01_connection_test.py` | Prueba de conexión a MySQL/MariaDB |
| `02_ATM_Database_Version.py` | Sistema ATM completo con base de datos |
| `03_create_atm_user.py` | Herramienta para crear/listar/eliminar usuarios ATM |
| `ATM_Database_Schema.sql` | Schema SQL para el sistema ATM |
| `python_exercises.sql` | Schema SQL alternativo |

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
mysql -u root -p ATM_Database_Schema < ATM_Database_Schema.sql
```

### Usuarios de Prueba

| Username | Password | Balance Inicial |
|----------|----------|-----------------|
| test_user | 1234 | $0.00 |
| florentino | 1234 | $1,000.00 |

### Uso

```bash
# Probar conexión
python 20_MySQL/01_connection_test.py

# Ejecutar sistema ATM
python 20_MySQL/02_ATM_Database_Version.py

# Gestionar usuarios (crear/listar/eliminar)
python 20_MySQL/03_create_atm_user.py
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

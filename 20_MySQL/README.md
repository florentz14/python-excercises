# 20_MySQL

Conexión y operaciones con bases de datos MySQL/MariaDB usando Python.

## Configuración

1. Crear archivo `.env` en la raíz del proyecto con:
   ```
   MYSQL_HOST=localhost
   MYSQL_USER=tu_usuario
   MYSQL_PASSWORD=tu_password
   MYSQL_DATABASE=python_exercises
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
| `03_create_atm_user.py` | Herramienta para crear usuarios ATM |
| `ATM_Database_Schema.sql` | Schema SQL para el sistema ATM |
| `corrected_database_schema.sql` | Schema SQL corregido |

## Sistema ATM con Base de Datos

### Características
- Autenticación de usuarios con contraseñas hasheadas (bcrypt)
- Depósitos y retiros con validación
- Historial completo de transacciones
- Exportación de historial a archivo
- Registro de sesiones y auditoría

### Instalación del Schema

```bash
# Desde la línea de comandos
mysql -u root -p python_exercises < ATM_Database_Schema.sql
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

# Ejecutar ATM
python 20_MySQL/02_ATM_Database_Version.py

# Crear usuarios
python 20_MySQL/03_create_atm_user.py
```

## Requisitos

- MySQL Server o MariaDB instalado y ejecutándose
- Base de datos creada
- Credenciales configuradas en `.env`
- Python 3.10+

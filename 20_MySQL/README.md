# 20_MySQL

Conexión y operaciones con bases de datos MySQL/MariaDB usando Python.

## Configuración

1. Crear archivo `.env` en la raíz del proyecto con:
   ```
   MYSQL_HOST=localhost
   MYSQL_USER=tu_usuario
   MYSQL_PASSWORD=tu_password
   MYSQL_DATABASE=nombre_base_datos
   MYSQL_PORT=3306
   ```

2. Instalar dependencias:
   ```bash
   pip install mysql-connector-python python-dotenv
   ```

## Archivos

| Archivo | Contenido |
|---------|-----------|
| `01_connection_test.py` | Prueba de conexión a MySQL/MariaDB |

## Uso

```bash
python 20_MySQL/01_connection_test.py
```

## Requisitos

- MySQL Server o MariaDB instalado y ejecutándose
- Base de datos creada
- Credenciales configuradas en `.env`

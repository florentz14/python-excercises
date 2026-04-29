# ATM MySQL App

Refactor modular del script `02_atm_mysql_app.py` siguiendo el patron de capas:

- `app/main.py` entrada principal
- `app/database.py` conexion y contexto MySQL
- `app/models/` entidades de dominio
- `app/schemas/` DTOs de entrada
- `app/services/` logica transaccional
- `app/routers/` menu/flujo CLI

## Ejecutar

Desde `20_Databases/atm_mysql_app`:

```bash
python ..\02_atm_mysql_app.py
```

Herramienta de administracion de usuarios:

```bash
python ..\03_atm_user_tool.py
```

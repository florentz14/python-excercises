# Books App

Estructura modular estilo `music_api` para los demos de libros de `20_Databases`.

## Estructura

- `app/main.py` entrada principal
- `app/database.py` configuracion de backends
- `app/models/` modelos base del dominio
- `app/schemas/` tipos de ejecucion
- `app/services/` ejecucion por backend
- `app/routers/` menu CLI

## Ejecutar

Desde `20_Databases`:

```bash
python -m books_app.app.main
```

o backend directo:

```bash
python -m books_app.app.main sqlite
python -m books_app.app.main postgres
python -m books_app.app.main sqlalchemy
python -m books_app.app.main mongo
python -m books_app.app.main example
```

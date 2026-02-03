# 09_Pandas

Tablas tipo Excel con **Pandas**: DataFrames, leer CSV, filtrar, columnas.

**Datos de ejemplo:** en la raíz del proyecto está `data.csv` (ventas por fecha, producto, categoría, región). Cargar desde la raíz: `pd.read_csv("data.csv")` o con ruta absoluta usando `Path(__file__).parent.parent / "data.csv"`.

| Archivo | Contenido |
|---------|-----------|
| `pandas_01_crear_dataframe.py` | Crear DataFrame desde diccionario |
| `pandas_02_leer_csv.py` | Leer CSV con `pd.read_csv()` |
| `pandas_03_filtrar.py` | Filtrar filas con condiciones |
| `pandas_04_columnas.py` | Seleccionar y crear columnas |

**Requisito:** `pip install pandas` (o `pip install -r requirements.txt` desde la raíz).

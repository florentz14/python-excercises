# 09_Pandas

Tablas tipo Excel con **Pandas**: DataFrames, leer CSV, filtrar, columnas. Incluye el **Sistema de Análisis de Rendimiento Estudiantil** sobre `StudentsPerformance.csv`.

---

## Datos de ejemplo

En la raíz del proyecto:

- **`data.csv`**: ventas (fecha, producto, categoría, región). Cargar: `Path(__file__).parent.parent / "data.csv"`.
- **`StudentsPerformance.csv`**: rendimiento estudiantil (género, grupo étnico, educación parental, almuerzo, preparación, math/reading/writing score). Usado por todos los análisis de esta carpeta.

---

## Archivos: ejercicios Pandas

| Archivo | Contenido |
|---------|-----------|
| `pandas_01_crear_dataframe.py` | Crear DataFrame desde diccionario |
| `pandas_02_leer_csv.py` | Leer CSV con `pd.read_csv()` (data.csv) |
| `pandas_03_filtrar.py` | Filtrar filas con condiciones |
| `pandas_04_columnas.py` | Seleccionar y crear columnas |

---

## Sistema de Análisis de Rendimiento Estudiantil

Conjunto de programas para analizar `StudentsPerformance.csv` desde distintas perspectivas.

| Archivo | Contenido |
|---------|-----------|
| **`menu_principal.py`** | **Menú interactivo**: ejecuta cualquier análisis o todos seguidos. Punto de entrada recomendado. |
| `analisis_general.py` | Estadísticas descriptivas, promedios por materia, distribución por rangos, correlación entre materias, estudiantes destacados y con dificultades |
| `analisis_por_genero.py` | Comparación por género: promedios, diferencias, variabilidad, estudiantes excelentes por género |
| `analisis_educacion_parental.py` | Impacto del nivel educativo de los padres: promedios, tendencias, universitarios vs no universitarios |
| `analisis_preparacion.py` | Impacto del curso de preparación: con/sin preparación, mejora por materia, análisis combinado con género |
| `analisis_almuerzo.py` | Tipo de almuerzo (indicador socioeconómico): standard vs free/reduced, brechas, interacción con género y preparación |
| `analisis_grupo_etnico.py` | Rendimiento por grupo étnico: promedios, ranking, brechas, interacción con educación y género |
| `analisis_students_performance.py` | Resumen único: carga CSV, estadísticas generales, promedios por categoría (género, almuerzo, preparación, educación), nota promedio global |

Todos los análisis leen el CSV desde la **raíz del proyecto**: `Path(__file__).parent.parent / "StudentsPerformance.csv"`.

---

## Requisitos

```bash
pip install pandas numpy
```

O desde la raíz del proyecto:

```bash
pip install -r requirements.txt
```

---

## Uso

### Opción 1: Menú interactivo (recomendado)

Desde la raíz del proyecto:

```bash
python 09_Pandas/menu_principal.py
```

Desde la carpeta `09_Pandas`:

```bash
python menu_principal.py
```

### Opción 2: Ejecutar análisis individuales

Desde la raíz (o desde `09_Pandas` con `python nombre_script.py`):

```bash
python 09_Pandas/analisis_general.py
python 09_Pandas/analisis_por_genero.py
python 09_Pandas/analisis_educacion_parental.py
python 09_Pandas/analisis_preparacion.py
python 09_Pandas/analisis_almuerzo.py
python 09_Pandas/analisis_grupo_etnico.py
python 09_Pandas/analisis_students_performance.py
```

---

## Estructura del dataset StudentsPerformance.csv

| Columna | Descripción |
|---------|-------------|
| **gender** | Género (male/female) |
| **race/ethnicity** | Grupo étnico (group A–E) |
| **parental level of education** | Nivel educativo de los padres |
| **lunch** | Tipo de almuerzo (standard / free/reduced) |
| **test preparation course** | Preparación para el examen (completed / none) |
| **math score** | Calificación matemáticas (0–100) |
| **reading score** | Calificación lectura (0–100) |
| **writing score** | Calificación escritura (0–100) |

---

## Resumen

- Ejercicios básicos: `pandas_01` a `pandas_04` + `analisis_students_performance.py` (un solo script de resumen).
- Sistema completo: `menu_principal.py` + 6 análisis temáticos (general, género, educación parental, preparación, almuerzo, grupo étnico).
- Los resultados se muestran en consola con formato tabular.

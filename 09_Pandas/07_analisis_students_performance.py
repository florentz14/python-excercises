"""
Análisis del archivo StudentsPerformance.csv
============================================
Carga el CSV, resume estadísticas y analiza notas por género, almuerzo,
preparación para el examen y nivel educativo de los padres.
"""

import pandas as pd
from pathlib import Path

# Ruta al CSV en la raíz del proyecto
RUTA_CSV = Path(__file__).parent.parent / "StudentsPerformance.csv"

def cargar_datos() -> pd.DataFrame:
    """Carga el CSV y convierte columnas de puntuación a numéricas."""
    df = pd.read_csv(RUTA_CSV, encoding="utf-8")
    # Asegurar que las puntuaciones son numéricas
    for col in ["math score", "reading score", "writing score"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def resumen_general(df: pd.DataFrame) -> None:
    """Muestra dimensiones, columnas, tipos y estadísticas descriptivas."""
    print("=" * 60)
    print("RESUMEN GENERAL")
    print("=" * 60)
    print(f"Filas: {len(df)}, Columnas: {len(df.columns)}")
    print("\nColumnas:", list(df.columns))
    print("\nTipos:\n", df.dtypes)
    print("\nEstadísticas descriptivas (notas):")
    columnas_notas = [c for c in df.columns if "score" in c]
    if columnas_notas:
        print(df[columnas_notas].describe().to_string())
    print("\nValores faltantes por columna:")
    print(df.isna().sum().to_string())


def promedios_por_categoria(df: pd.DataFrame) -> None:
    """Promedio de notas por género, almuerzo, preparación y educación de padres."""
    columnas_notas = [c for c in df.columns if "score" in c]
    if not columnas_notas:
        return

    print("\n" + "=" * 60)
    print("PROMEDIOS POR CATEGORÍA")
    print("=" * 60)

    # Por género
    if "gender" in df.columns:
        print("\n--- Por género ---")
        print(df.groupby("gender")[columnas_notas].mean().round(2).to_string())

    # Por tipo de almuerzo
    if "lunch" in df.columns:
        print("\n--- Por tipo de almuerzo ---")
        print(df.groupby("lunch")[columnas_notas].mean().round(2).to_string())

    # Por preparación para el examen
    col_prep = "test preparation course"
    if col_prep in df.columns:
        print("\n--- Por preparación para el examen ---")
        print(df.groupby(col_prep)[columnas_notas].mean().round(2).to_string())

    # Por nivel educativo de los padres
    col_edu = "parental level of education"
    if col_edu in df.columns:
        print("\n--- Por nivel educativo de los padres ---")
        print(df.groupby(col_edu)[columnas_notas].mean().round(2).to_string())


def nota_promedio_global(df: pd.DataFrame) -> None:
    """Crea columna 'average score' y muestra resumen."""
    columnas_notas = [c for c in df.columns if "score" in c]
    if not columnas_notas:
        return
    df["average score"] = df[columnas_notas].mean(axis=1)
    print("\n" + "=" * 60)
    print("NOTA PROMEDIO GLOBAL (math, reading, writing)")
    print("=" * 60)
    print(df["average score"].describe().to_string())


def main() -> None:
    if not RUTA_CSV.is_file():
        print(f"No se encontró el archivo: {RUTA_CSV}")
        return

    df = cargar_datos()
    resumen_general(df)
    promedios_por_categoria(df)
    nota_promedio_global(df)
    print("\n" + "=" * 60)
    print("Análisis completado.")
    print("=" * 60)


if __name__ == "__main__":
    main()

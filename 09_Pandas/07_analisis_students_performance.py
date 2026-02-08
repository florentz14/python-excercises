# -------------------------------------------------
# File Name: 07_analisis_students_performance.py
# Author: Florentino Báez
# Date: Pandas
# Description: Students Performance CSV Analysis.
#              Loads StudentsPerformance.csv, shows descriptive
#              statistics, computes averages by gender, lunch
#              type, test preparation, and parental education.
#              Calculates a global average score column.
# -------------------------------------------------

"""
StudentsPerformance.csv Analysis
================================
Loads the CSV, summarizes statistics and analyzes scores by gender, lunch,
test preparation, and parental education level.
"""

import pandas as pd
from pathlib import Path

# Path to CSV in project root
RUTA_CSV = Path(__file__).parent.parent / "StudentsPerformance.csv"

def cargar_datos() -> pd.DataFrame:
    """Loads the CSV and converts score columns to numeric."""
    df = pd.read_csv(RUTA_CSV, encoding="utf-8")
    # Ensure scores are numeric
    for col in ["math score", "reading score", "writing score"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def resumen_general(df: pd.DataFrame) -> None:
    """Shows dimensions, columns, types and descriptive statistics."""
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
    """Average scores by gender, lunch, preparation and parental education."""
    columnas_notas = [c for c in df.columns if "score" in c]
    if not columnas_notas:
        return

    print("\n" + "=" * 60)
    print("PROMEDIOS POR CATEGORÍA")
    print("=" * 60)

    # By gender
    if "gender" in df.columns:
        print("\n--- Por género ---")
        print(df.groupby("gender")[columnas_notas].mean().round(2).to_string())

    # By lunch type
    if "lunch" in df.columns:
        print("\n--- Por tipo de almuerzo ---")
        print(df.groupby("lunch")[columnas_notas].mean().round(2).to_string())

    # By test preparation
    col_prep = "test preparation course"
    if col_prep in df.columns:
        print("\n--- Por preparación para el examen ---")
        print(df.groupby(col_prep)[columnas_notas].mean().round(2).to_string())

    # By parental education level
    col_edu = "parental level of education"
    if col_edu in df.columns:
        print("\n--- Por nivel educativo de los padres ---")
        print(df.groupby(col_edu)[columnas_notas].mean().round(2).to_string())


def nota_promedio_global(df: pd.DataFrame) -> None:
    """Creates 'average score' column and shows summary."""
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

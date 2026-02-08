# -------------------------------------------------
# File Name: 05_analisis_por_genero.py
# Author: Florentino Báez
# Date: Pandas
# Description: Gender Performance Analysis.
#              Compares academic performance between male and
#              female students. Calculates per-subject gaps,
#              high-score distribution, and standard deviation
#              by gender.
# -------------------------------------------------

"""
Gender Performance Analysis
Compares academic performance between male and female students
"""

import pandas as pd
import numpy as np

def analisis_por_genero(archivo_csv):
    """Analyzes academic performance comparing genders"""
    
    df = pd.read_csv(archivo_csv)
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
    
    print("=" * 80)
    print("ANÁLISIS DE RENDIMIENTO POR GÉNERO")
    print("=" * 80)
    
    # Gender distribution
    print("\n👥 DISTRIBUCIÓN DE ESTUDIANTES")
    print("-" * 80)
    distribucion = df['gender'].value_counts()
    for genero, count in distribucion.items():
        porcentaje = (count / len(df)) * 100
        print(f"{genero.capitalize():8}: {count:3d} estudiantes ({porcentaje:.2f}%)")
    
    # Averages by gender
    print("\n\n📊 PROMEDIO DE CALIFICACIONES POR GÉNERO")
    print("-" * 80)
    print(f"{'':15} {'Matemáticas':>12} {'Lectura':>12} {'Escritura':>12} {'Promedio':>12}")
    print("-" * 80)
    
    for genero in df['gender'].unique():
        df_genero = df[df['gender'] == genero]
        math_avg = df_genero['math score'].mean()
        reading_avg = df_genero['reading score'].mean()
        writing_avg = df_genero['writing score'].mean()
        total_avg = df_genero['average_score'].mean()
        
        print(f"{genero.capitalize():15} {math_avg:12.2f} {reading_avg:12.2f} {writing_avg:12.2f} {total_avg:12.2f}")
    
    # Differences between genders
    print("\n\n📈 DIFERENCIAS ENTRE GÉNEROS")
    print("-" * 80)
    male_avg = df[df['gender'] == 'male']['math score'].mean()
    female_avg = df[df['gender'] == 'female']['math score'].mean()
    diff_math = male_avg - female_avg
    
    male_reading = df[df['gender'] == 'male']['reading score'].mean()
    female_reading = df[df['gender'] == 'female']['reading score'].mean()
    diff_reading = male_reading - female_reading
    
    male_writing = df[df['gender'] == 'male']['writing score'].mean()
    female_writing = df[df['gender'] == 'female']['writing score'].mean()
    diff_writing = male_writing - female_writing
    
    print(f"Matemáticas: {'Hombres' if diff_math > 0 else 'Mujeres'} superan por {abs(diff_math):.2f} puntos")
    print(f"Lectura:     {'Hombres' if diff_reading > 0 else 'Mujeres'} superan por {abs(diff_reading):.2f} puntos")
    print(f"Escritura:   {'Hombres' if diff_writing > 0 else 'Mujeres'} superan por {abs(diff_writing):.2f} puntos")
    
    # High score distribution
    print("\n\n🏆 ESTUDIANTES CON CALIFICACIONES EXCELENTES (≥85)")
    print("-" * 80)
    
    for materia in ['math score', 'reading score', 'writing score']:
        print(f"\n{materia.replace(' score', '').capitalize()}:")
        for genero in df['gender'].unique():
            df_genero = df[df['gender'] == genero]
            count_high = (df_genero[materia] >= 85).sum()
            porcentaje = (count_high / len(df_genero)) * 100
            print(f"  {genero.capitalize():8}: {count_high:3d} estudiantes ({porcentaje:5.2f}%)")
    
    # Standard deviation by gender
    print("\n\n📉 VARIABILIDAD (Desviación Estándar)")
    print("-" * 80)
    print(f"{'':15} {'Matemáticas':>12} {'Lectura':>12} {'Escritura':>12}")
    print("-" * 80)
    
    for genero in df['gender'].unique():
        df_genero = df[df['gender'] == genero]
        math_std = df_genero['math score'].std()
        reading_std = df_genero['reading score'].std()
        writing_std = df_genero['writing score'].std()
        
        print(f"{genero.capitalize():15} {math_std:12.2f} {reading_std:12.2f} {writing_std:12.2f}")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    from pathlib import Path
    archivo = Path(__file__).parent.parent / "StudentsPerformance.csv"
    analisis_por_genero(archivo)

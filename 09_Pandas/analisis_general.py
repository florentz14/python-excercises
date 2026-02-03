"""
Análisis General de Rendimiento Estudiantil
Este programa proporciona estadísticas descriptivas generales del dataset
"""

import pandas as pd
import numpy as np

def analisis_general(archivo_csv):
    """Realiza un análisis estadístico general del dataset"""
    
    # Cargar datos
    df = pd.read_csv(archivo_csv)
    
    print("=" * 80)
    print("ANÁLISIS GENERAL DE RENDIMIENTO ESTUDIANTIL")
    print("=" * 80)
    
    # Información básica del dataset
    print("\n📊 INFORMACIÓN DEL DATASET")
    print("-" * 80)
    print(f"Total de estudiantes: {len(df)}")
    print(f"Número de columnas: {len(df.columns)}")
    print(f"\nColumnas disponibles:")
    for col in df.columns:
        print(f"  - {col}")
    
    # Estadísticas descriptivas de las calificaciones
    print("\n\n📈 ESTADÍSTICAS DESCRIPTIVAS DE CALIFICACIONES")
    print("-" * 80)
    scores = df[['math score', 'reading score', 'writing score']]
    print(scores.describe())
    
    # Promedio general por materia
    print("\n\n📚 PROMEDIO GENERAL POR MATERIA")
    print("-" * 80)
    print(f"Matemáticas: {df['math score'].mean():.2f}")
    print(f"Lectura:     {df['reading score'].mean():.2f}")
    print(f"Escritura:   {df['writing score'].mean():.2f}")
    
    # Calcular promedio total
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
    print(f"\nPromedio Total: {df['average_score'].mean():.2f}")
    
    # Distribución de calificaciones
    print("\n\n📊 DISTRIBUCIÓN DE CALIFICACIONES")
    print("-" * 80)
    rangos = [(0, 50, 'Bajo'), (50, 70, 'Medio'), (70, 85, 'Alto'), (85, 100, 'Excelente')]
    
    for materia in ['math score', 'reading score', 'writing score']:
        print(f"\n{materia.replace(' score', '').capitalize()}:")
        for min_val, max_val, categoria in rangos:
            count = ((df[materia] >= min_val) & (df[materia] < max_val)).sum()
            porcentaje = (count / len(df)) * 100
            print(f"  {categoria:12} ({min_val:2d}-{max_val:2d}): {count:3d} estudiantes ({porcentaje:5.2f}%)")
    
    # Estudiantes con mejor y peor rendimiento
    print("\n\n🏆 ESTUDIANTES DESTACADOS")
    print("-" * 80)
    mejor_idx = df['average_score'].idxmax()
    peor_idx = df['average_score'].idxmin()
    
    print("Mejor estudiante:")
    print(f"  Promedio: {df.loc[mejor_idx, 'average_score']:.2f}")
    print(f"  Matemáticas: {df.loc[mejor_idx, 'math score']}")
    print(f"  Lectura: {df.loc[mejor_idx, 'reading score']}")
    print(f"  Escritura: {df.loc[mejor_idx, 'writing score']}")
    
    print("\nEstudiante con más dificultades:")
    print(f"  Promedio: {df.loc[peor_idx, 'average_score']:.2f}")
    print(f"  Matemáticas: {df.loc[peor_idx, 'math score']}")
    print(f"  Lectura: {df.loc[peor_idx, 'reading score']}")
    print(f"  Escritura: {df.loc[peor_idx, 'writing score']}")
    
    # Correlación entre materias
    print("\n\n🔗 CORRELACIÓN ENTRE MATERIAS")
    print("-" * 80)
    correlation = scores.corr()
    print(correlation)
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    from pathlib import Path
    archivo = Path(__file__).parent.parent / "StudentsPerformance.csv"
    analisis_general(archivo)

"""
Análisis del Impacto de la Preparación para Exámenes
Evalúa cómo el curso de preparación afecta el rendimiento estudiantil
"""

import pandas as pd
import numpy as np

def analisis_preparacion_examenes(archivo_csv):
    """Analiza el impacto del curso de preparación para exámenes"""
    
    df = pd.read_csv(archivo_csv)
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
    
    print("=" * 80)
    print("ANÁLISIS DEL IMPACTO DE LA PREPARACIÓN PARA EXÁMENES")
    print("=" * 80)
    
    # Distribución de estudiantes
    print("\n📚 DISTRIBUCIÓN DE ESTUDIANTES")
    print("-" * 80)
    distribucion = df['test preparation course'].value_counts()
    for status, count in distribucion.items():
        porcentaje = (count / len(df)) * 100
        print(f"{status.capitalize():15}: {count:3d} estudiantes ({porcentaje:.2f}%)")
    
    # Promedios comparativos
    print("\n\n📊 COMPARACIÓN DE CALIFICACIONES")
    print("-" * 80)
    print(f"{'Preparación':15} {'Matemáticas':>12} {'Lectura':>12} {'Escritura':>12} {'Promedio':>12}")
    print("-" * 80)
    
    resultados = {}
    for status in df['test preparation course'].unique():
        df_status = df[df['test preparation course'] == status]
        math_avg = df_status['math score'].mean()
        reading_avg = df_status['reading score'].mean()
        writing_avg = df_status['writing score'].mean()
        total_avg = df_status['average_score'].mean()
        
        resultados[status] = {
            'math': math_avg,
            'reading': reading_avg,
            'writing': writing_avg,
            'total': total_avg
        }
        
        print(f"{status.capitalize():15} {math_avg:12.2f} {reading_avg:12.2f} {writing_avg:12.2f} {total_avg:12.2f}")
    
    # Impacto de la preparación
    print("\n\n📈 IMPACTO DE LA PREPARACIÓN")
    print("-" * 80)
    
    if 'completed' in resultados and 'none' in resultados:
        mejora_math = resultados['completed']['math'] - resultados['none']['math']
        mejora_reading = resultados['completed']['reading'] - resultados['none']['reading']
        mejora_writing = resultados['completed']['writing'] - resultados['none']['writing']
        mejora_total = resultados['completed']['total'] - resultados['none']['total']
        
        print("Mejora promedio con preparación:")
        print(f"  Matemáticas: {mejora_math:+.2f} puntos")
        print(f"  Lectura:     {mejora_reading:+.2f} puntos")
        print(f"  Escritura:   {mejora_writing:+.2f} puntos")
        print(f"  Promedio:    {mejora_total:+.2f} puntos")
        
        # Calcular porcentaje de mejora
        pct_mejora = (mejora_total / resultados['none']['total']) * 100
        print(f"\n  → Mejora porcentual: {pct_mejora:+.2f}%")
    
    # Distribución de calificaciones altas
    print("\n\n🏆 ESTUDIANTES CON CALIFICACIONES EXCELENTES (≥85)")
    print("-" * 80)
    
    for status in df['test preparation course'].unique():
        df_status = df[df['test preparation course'] == status]
        print(f"\n{status.capitalize()}:")
        
        for materia in ['math score', 'reading score', 'writing score']:
            count_high = (df_status[materia] >= 85).sum()
            porcentaje = (count_high / len(df_status)) * 100
            print(f"  {materia.replace(' score', '').capitalize():12}: {count_high:3d} estudiantes ({porcentaje:5.2f}%)")
    
    # Análisis por género y preparación
    print("\n\n👥 IMPACTO DE LA PREPARACIÓN POR GÉNERO")
    print("-" * 80)
    
    for genero in df['gender'].unique():
        print(f"\n{genero.capitalize()}:")
        df_genero = df[df['gender'] == genero]
        
        for status in df['test preparation course'].unique():
            df_combined = df_genero[df_genero['test preparation course'] == status]
            if len(df_combined) > 0:
                avg_score = df_combined['average_score'].mean()
                count = len(df_combined)
                print(f"  {status.capitalize():15}: {avg_score:6.2f} puntos ({count:3d} estudiantes)")
    
    # Estudiantes con bajo rendimiento
    print("\n\n⚠️  ESTUDIANTES CON DIFICULTADES (Promedio <60)")
    print("-" * 80)
    
    for status in df['test preparation course'].unique():
        df_status = df[df['test preparation course'] == status]
        count_low = (df_status['average_score'] < 60).sum()
        porcentaje = (count_low / len(df_status)) * 100
        print(f"{status.capitalize():15}: {count_low:3d} estudiantes ({porcentaje:5.2f}%)")
    
    # Recomendación
    print("\n\n💡 CONCLUSIÓN")
    print("-" * 80)
    if 'completed' in resultados and 'none' in resultados:
        if mejora_total > 0:
            print(f"El curso de preparación muestra un impacto positivo de {mejora_total:.2f} puntos")
            print("en el promedio general. Se recomienda fomentar la participación en estos cursos.")
        else:
            print("Los datos no muestran una mejora significativa con el curso de preparación.")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    from pathlib import Path
    archivo = Path(__file__).parent.parent / "StudentsPerformance.csv"
    analisis_preparacion_examenes(archivo)

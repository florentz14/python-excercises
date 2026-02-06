"""
Análisis por Tipo de Almuerzo (Indicador Socioeconómico)
Examina cómo el tipo de almuerzo (estándar vs gratuito/reducido) afecta el rendimiento
"""

import pandas as pd
import numpy as np

def analisis_por_almuerzo(archivo_csv):
    """Analiza el impacto del tipo de almuerzo en el rendimiento estudiantil"""
    
    df = pd.read_csv(archivo_csv)
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
    
    print("=" * 80)
    print("ANÁLISIS POR TIPO DE ALMUERZO (INDICADOR SOCIOECONÓMICO)")
    print("=" * 80)
    
    # Distribución
    print("\n🍽️  DISTRIBUCIÓN DE ESTUDIANTES")
    print("-" * 80)
    distribucion = df['lunch'].value_counts()
    for tipo, count in distribucion.items():
        porcentaje = (count / len(df)) * 100
        print(f"{tipo.capitalize():15}: {count:3d} estudiantes ({porcentaje:.2f}%)")
    
    # Promedios comparativos
    print("\n\n📊 COMPARACIÓN DE CALIFICACIONES POR TIPO DE ALMUERZO")
    print("-" * 80)
    print(f"{'Tipo de Almuerzo':15} {'Matemáticas':>12} {'Lectura':>12} {'Escritura':>12} {'Promedio':>12}")
    print("-" * 80)
    
    resultados = {}
    for tipo in df['lunch'].unique():
        df_tipo = df[df['lunch'] == tipo]
        math_avg = df_tipo['math score'].mean()
        reading_avg = df_tipo['reading score'].mean()
        writing_avg = df_tipo['writing score'].mean()
        total_avg = df_tipo['average_score'].mean()
        
        resultados[tipo] = {
            'math': math_avg,
            'reading': reading_avg,
            'writing': writing_avg,
            'total': total_avg,
            'count': len(df_tipo)
        }
        
        print(f"{tipo.capitalize():15} {math_avg:12.2f} {reading_avg:12.2f} {writing_avg:12.2f} {total_avg:12.2f}")
    
    # Brecha de rendimiento
    print("\n\n📉 BRECHA DE RENDIMIENTO")
    print("-" * 80)
    
    if 'standard' in resultados and 'free/reduced' in resultados:
        brecha_math = resultados['standard']['math'] - resultados['free/reduced']['math']
        brecha_reading = resultados['standard']['reading'] - resultados['free/reduced']['reading']
        brecha_writing = resultados['standard']['writing'] - resultados['free/reduced']['writing']
        brecha_total = resultados['standard']['total'] - resultados['free/reduced']['total']
        
        print("Diferencia (Standard - Free/Reduced):")
        print(f"  Matemáticas: {brecha_math:+.2f} puntos")
        print(f"  Lectura:     {brecha_reading:+.2f} puntos")
        print(f"  Escritura:   {brecha_writing:+.2f} puntos")
        print(f"  Promedio:    {brecha_total:+.2f} puntos")
        
        # Porcentaje de la brecha
        pct_brecha = (brecha_total / resultados['free/reduced']['total']) * 100
        print(f"\n  → Brecha porcentual: {pct_brecha:.2f}%")
    
    # Distribución de calificaciones
    print("\n\n📊 DISTRIBUCIÓN POR RANGOS DE CALIFICACIÓN")
    print("-" * 80)
    
    rangos = [(0, 60, 'Bajo'), (60, 75, 'Medio'), (75, 90, 'Alto'), (90, 100, 'Excelente')]
    
    for tipo in df['lunch'].unique():
        df_tipo = df[df['lunch'] == tipo]
        print(f"\n{tipo.capitalize()}:")
        
        for min_val, max_val, categoria in rangos:
            count = ((df_tipo['average_score'] >= min_val) & (df_tipo['average_score'] < max_val)).sum()
            porcentaje = (count / len(df_tipo)) * 100
            print(f"  {categoria:12} ({min_val:2d}-{max_val:2d}): {count:3d} estudiantes ({porcentaje:5.2f}%)")
    
    # Análisis por género y tipo de almuerzo
    print("\n\n👥 ANÁLISIS POR GÉNERO Y TIPO DE ALMUERZO")
    print("-" * 80)
    
    for genero in df['gender'].unique():
        print(f"\n{genero.capitalize()}:")
        df_genero = df[df['gender'] == genero]
        
        for tipo in df['lunch'].unique():
            df_combined = df_genero[df_genero['lunch'] == tipo]
            if len(df_combined) > 0:
                avg_score = df_combined['average_score'].mean()
                count = len(df_combined)
                print(f"  {tipo.capitalize():15}: {avg_score:6.2f} puntos ({count:3d} estudiantes)")
    
    # Estudiantes destacados
    print("\n\n🏆 ESTUDIANTES CON PROMEDIO ≥85")
    print("-" * 80)
    
    for tipo in df['lunch'].unique():
        df_tipo = df[df['lunch'] == tipo]
        count_high = (df_tipo['average_score'] >= 85).sum()
        porcentaje = (count_high / len(df_tipo)) * 100
        print(f"{tipo.capitalize():15}: {count_high:3d} estudiantes ({porcentaje:5.2f}%)")
    
    # Preparación para exámenes y almuerzo
    print("\n\n📚 INTERACCIÓN: PREPARACIÓN Y TIPO DE ALMUERZO")
    print("-" * 80)
    
    for tipo_almuerzo in df['lunch'].unique():
        print(f"\n{tipo_almuerzo.capitalize()}:")
        df_almuerzo = df[df['lunch'] == tipo_almuerzo]
        
        for prep in df['test preparation course'].unique():
            df_combined = df_almuerzo[df_almuerzo['test preparation course'] == prep]
            if len(df_combined) > 0:
                avg_score = df_combined['average_score'].mean()
                count = len(df_combined)
                print(f"  Preparación {prep:10}: {avg_score:6.2f} puntos ({count:3d} estudiantes)")
    
    # Variabilidad
    print("\n\n📈 VARIABILIDAD (Desviación Estándar)")
    print("-" * 80)
    
    for tipo in df['lunch'].unique():
        df_tipo = df[df['lunch'] == tipo]
        std_score = df_tipo['average_score'].std()
        print(f"{tipo.capitalize():15}: {std_score:.2f}")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    from pathlib import Path
    archivo = Path(__file__).parent.parent / "StudentsPerformance.csv"
    analisis_por_almuerzo(archivo)

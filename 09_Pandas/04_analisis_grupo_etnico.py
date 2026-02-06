"""
Análisis de Rendimiento por Grupo Étnico
Examina las diferencias de rendimiento entre diferentes grupos étnicos
"""

import pandas as pd
import numpy as np

def analisis_por_grupo_etnico(archivo_csv):
    """Analiza el rendimiento académico por grupo étnico"""
    
    df = pd.read_csv(archivo_csv)
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
    
    print("=" * 90)
    print("ANÁLISIS DE RENDIMIENTO POR GRUPO ÉTNICO")
    print("=" * 90)
    
    # Distribución de grupos
    print("\n🌍 DISTRIBUCIÓN DE GRUPOS ÉTNICOS")
    print("-" * 90)
    distribucion = df['race/ethnicity'].value_counts().sort_index()
    for grupo, count in distribucion.items():
        porcentaje = (count / len(df)) * 100
        print(f"{grupo:15}: {count:3d} estudiantes ({porcentaje:.2f}%)")
    
    # Promedios por grupo
    print("\n\n📊 PROMEDIO DE CALIFICACIONES POR GRUPO ÉTNICO")
    print("-" * 90)
    print(f"{'Grupo':15} {'Matemáticas':>12} {'Lectura':>12} {'Escritura':>12} {'Promedio':>12} {'N':>8}")
    print("-" * 90)
    
    resultados = []
    for grupo in sorted(df['race/ethnicity'].unique()):
        df_grupo = df[df['race/ethnicity'] == grupo]
        math_avg = df_grupo['math score'].mean()
        reading_avg = df_grupo['reading score'].mean()
        writing_avg = df_grupo['writing score'].mean()
        total_avg = df_grupo['average_score'].mean()
        count = len(df_grupo)
        
        resultados.append({
            'grupo': grupo,
            'math': math_avg,
            'reading': reading_avg,
            'writing': writing_avg,
            'total': total_avg,
            'count': count
        })
        
        print(f"{grupo:15} {math_avg:12.2f} {reading_avg:12.2f} {writing_avg:12.2f} {total_avg:12.2f} {count:8d}")
    
    # Ranking de grupos
    print("\n\n🏆 RANKING POR RENDIMIENTO PROMEDIO")
    print("-" * 90)
    
    resultados_ordenados = sorted(resultados, key=lambda x: x['total'], reverse=True)
    for i, resultado in enumerate(resultados_ordenados, 1):
        print(f"{i}. {resultado['grupo']:15} - {resultado['total']:.2f} puntos")
    
    # Análisis de brechas
    print("\n\n📉 BRECHAS DE RENDIMIENTO")
    print("-" * 90)
    
    mejor_grupo = resultados_ordenados[0]
    peor_grupo = resultados_ordenados[-1]
    
    print(f"Grupo con mejor rendimiento:  {mejor_grupo['grupo']:15} ({mejor_grupo['total']:.2f})")
    print(f"Grupo con menor rendimiento:  {peor_grupo['grupo']:15} ({peor_grupo['total']:.2f})")
    print(f"Brecha total:                 {mejor_grupo['total'] - peor_grupo['total']:.2f} puntos")
    
    brecha_math = mejor_grupo['math'] - peor_grupo['math']
    brecha_reading = mejor_grupo['reading'] - peor_grupo['reading']
    brecha_writing = mejor_grupo['writing'] - peor_grupo['writing']
    
    print(f"\nBrechas por materia:")
    print(f"  Matemáticas: {brecha_math:.2f} puntos")
    print(f"  Lectura:     {brecha_reading:.2f} puntos")
    print(f"  Escritura:   {brecha_writing:.2f} puntos")
    
    # Estudiantes destacados por grupo
    print("\n\n🌟 ESTUDIANTES CON PROMEDIO ≥85 POR GRUPO")
    print("-" * 90)
    
    for grupo in sorted(df['race/ethnicity'].unique()):
        df_grupo = df[df['race/ethnicity'] == grupo]
        count_high = (df_grupo['average_score'] >= 85).sum()
        porcentaje = (count_high / len(df_grupo)) * 100
        print(f"{grupo:15}: {count_high:3d} estudiantes ({porcentaje:5.2f}%)")
    
    # Distribución de calificaciones por grupo
    print("\n\n📊 DISTRIBUCIÓN DE RENDIMIENTO POR GRUPO")
    print("-" * 90)
    
    rangos = [(0, 60, 'Bajo'), (60, 75, 'Medio'), (75, 90, 'Alto'), (90, 100, 'Excelente')]
    
    for grupo in sorted(df['race/ethnicity'].unique()):
        df_grupo = df[df['race/ethnicity'] == grupo]
        print(f"\n{grupo}:")
        
        for min_val, max_val, categoria in rangos:
            count = ((df_grupo['average_score'] >= min_val) & (df_grupo['average_score'] < max_val)).sum()
            porcentaje = (count / len(df_grupo)) * 100
            print(f"  {categoria:12} ({min_val:2d}-{max_val:2d}): {count:3d} estudiantes ({porcentaje:5.2f}%)")
    
    # Interacción con otros factores
    print("\n\n🔗 INTERACCIÓN: GRUPO ÉTNICO Y EDUCACIÓN PARENTAL")
    print("-" * 90)
    
    # Grupos con mayor proporción de educación universitaria parental
    niveles_uni = ["some college", "associate's degree", "bachelor's degree", "master's degree"]
    
    for grupo in sorted(df['race/ethnicity'].unique()):
        df_grupo = df[df['race/ethnicity'] == grupo]
        count_uni = df_grupo[df_grupo['parental level of education'].isin(niveles_uni)].shape[0]
        porcentaje = (count_uni / len(df_grupo)) * 100
        avg_uni = df_grupo[df_grupo['parental level of education'].isin(niveles_uni)]['average_score'].mean()
        
        print(f"{grupo:15}: {porcentaje:5.2f}% con educación universitaria (promedio: {avg_uni:.2f})")
    
    # Análisis de género por grupo étnico
    print("\n\n👥 PROMEDIO POR GRUPO ÉTNICO Y GÉNERO")
    print("-" * 90)
    
    for grupo in sorted(df['race/ethnicity'].unique()):
        print(f"\n{grupo}:")
        df_grupo = df[df['race/ethnicity'] == grupo]
        
        for genero in df['gender'].unique():
            df_combined = df_grupo[df_grupo['gender'] == genero]
            if len(df_combined) > 0:
                avg_score = df_combined['average_score'].mean()
                count = len(df_combined)
                print(f"  {genero.capitalize():8}: {avg_score:6.2f} puntos ({count:3d} estudiantes)")
    
    print("\n" + "=" * 90)

if __name__ == "__main__":
    from pathlib import Path
    archivo = Path(__file__).parent.parent / "StudentsPerformance.csv"
    analisis_por_grupo_etnico(archivo)

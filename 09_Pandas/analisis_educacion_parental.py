"""
Análisis de Rendimiento según Nivel Educativo de los Padres
Examina cómo el nivel educativo de los padres afecta el rendimiento estudiantil
"""

import pandas as pd
import numpy as np

def analisis_por_educacion_parental(archivo_csv):
    """Analiza el impacto del nivel educativo de los padres en el rendimiento"""
    
    df = pd.read_csv(archivo_csv)
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
    
    print("=" * 90)
    print("ANÁLISIS DE RENDIMIENTO SEGÚN NIVEL EDUCATIVO DE LOS PADRES")
    print("=" * 90)
    
    # Distribución de niveles educativos
    print("\n🎓 DISTRIBUCIÓN DE NIVELES EDUCATIVOS PARENTALES")
    print("-" * 90)
    distribucion = df['parental level of education'].value_counts().sort_values(ascending=False)
    for nivel, count in distribucion.items():
        porcentaje = (count / len(df)) * 100
        print(f"{nivel:25}: {count:3d} estudiantes ({porcentaje:5.2f}%)")
    
    # Ordenar niveles educativos de menor a mayor
    orden_educativo = [
        'some high school',
        'high school',
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
    
    # Filtrar solo los niveles que existen en los datos
    niveles_disponibles = [n for n in orden_educativo if n in df['parental level of education'].unique()]
    
    # Promedios por nivel educativo
    print("\n\n📊 PROMEDIO DE CALIFICACIONES POR NIVEL EDUCATIVO PARENTAL")
    print("-" * 90)
    print(f"{'Nivel Educativo':25} {'Matemáticas':>12} {'Lectura':>12} {'Escritura':>12} {'Promedio':>12}")
    print("-" * 90)
    
    resultados = []
    for nivel in niveles_disponibles:
        df_nivel = df[df['parental level of education'] == nivel]
        math_avg = df_nivel['math score'].mean()
        reading_avg = df_nivel['reading score'].mean()
        writing_avg = df_nivel['writing score'].mean()
        total_avg = df_nivel['average_score'].mean()
        
        resultados.append({
            'nivel': nivel,
            'math': math_avg,
            'reading': reading_avg,
            'writing': writing_avg,
            'total': total_avg
        })
        
        print(f"{nivel:25} {math_avg:12.2f} {reading_avg:12.2f} {writing_avg:12.2f} {total_avg:12.2f}")
    
    # Análisis de tendencias
    print("\n\n📈 TENDENCIA: NIVEL EDUCATIVO vs RENDIMIENTO")
    print("-" * 90)
    
    if len(resultados) >= 2:
        mejor_nivel = max(resultados, key=lambda x: x['total'])
        peor_nivel = min(resultados, key=lambda x: x['total'])
        
        print(f"Mejor rendimiento promedio:  {mejor_nivel['nivel']:25} ({mejor_nivel['total']:.2f})")
        print(f"Menor rendimiento promedio:  {peor_nivel['nivel']:25} ({peor_nivel['total']:.2f})")
        print(f"Diferencia:                  {mejor_nivel['total'] - peor_nivel['total']:.2f} puntos")
    
    # Comparación: con estudios universitarios vs sin estudios universitarios
    print("\n\n🎯 COMPARACIÓN: ESTUDIOS UNIVERSITARIOS vs NO UNIVERSITARIOS")
    print("-" * 90)
    
    universitarios = ["some college", "associate's degree", "bachelor's degree", "master's degree"]
    no_universitarios = ["some high school", "high school"]
    
    df_uni = df[df['parental level of education'].isin(universitarios)]
    df_no_uni = df[df['parental level of education'].isin(no_universitarios)]
    
    if len(df_uni) > 0 and len(df_no_uni) > 0:
        print(f"\nCon estudios universitarios ({len(df_uni)} estudiantes):")
        print(f"  Promedio general: {df_uni['average_score'].mean():.2f}")
        print(f"  Matemáticas: {df_uni['math score'].mean():.2f}")
        print(f"  Lectura: {df_uni['reading score'].mean():.2f}")
        print(f"  Escritura: {df_uni['writing score'].mean():.2f}")
        
        print(f"\nSin estudios universitarios ({len(df_no_uni)} estudiantes):")
        print(f"  Promedio general: {df_no_uni['average_score'].mean():.2f}")
        print(f"  Matemáticas: {df_no_uni['math score'].mean():.2f}")
        print(f"  Lectura: {df_no_uni['reading score'].mean():.2f}")
        print(f"  Escritura: {df_no_uni['writing score'].mean():.2f}")
        
        diferencia = df_uni['average_score'].mean() - df_no_uni['average_score'].mean()
        print(f"\n  → Diferencia a favor de estudios universitarios: {diferencia:.2f} puntos")
    
    # Estudiantes destacados por nivel educativo
    print("\n\n🏆 ESTUDIANTES CON PROMEDIO ≥80 POR NIVEL EDUCATIVO")
    print("-" * 90)
    
    for nivel in niveles_disponibles:
        df_nivel = df[df['parental level of education'] == nivel]
        count_high = (df_nivel['average_score'] >= 80).sum()
        porcentaje = (count_high / len(df_nivel)) * 100 if len(df_nivel) > 0 else 0
        print(f"{nivel:25}: {count_high:3d} estudiantes ({porcentaje:5.2f}%)")
    
    print("\n" + "=" * 90)

if __name__ == "__main__":
    from pathlib import Path
    archivo = Path(__file__).parent.parent / "StudentsPerformance.csv"
    analisis_por_educacion_parental(archivo)

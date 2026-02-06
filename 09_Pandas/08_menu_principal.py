"""
Programa Maestro de Análisis de Rendimiento Estudiantil
Ejecuta todos los análisis disponibles con un menú interactivo
"""

import subprocess
import sys
from pathlib import Path

# Carpeta donde está este script (09_Pandas); los análisis se ejecutan desde aquí
CARPETA_PANDAS = Path(__file__).resolve().parent

def mostrar_menu():
    """Muestra el menú principal de opciones"""
    print("\n" + "=" * 80)
    print("SISTEMA DE ANÁLISIS DE RENDIMIENTO ESTUDIANTIL")
    print("=" * 80)
    print("\nSeleccione el tipo de análisis que desea realizar:")
    print("\n1. Análisis General")
    print("   - Estadísticas descriptivas generales")
    print("   - Promedios por materia")
    print("   - Distribución de calificaciones")
    print("   - Correlaciones entre materias")
    
    print("\n2. Análisis por Género")
    print("   - Comparación de rendimiento entre géneros")
    print("   - Diferencias por materia")
    print("   - Distribución de calificaciones altas")
    
    print("\n3. Análisis por Educación Parental")
    print("   - Impacto del nivel educativo de los padres")
    print("   - Tendencias de rendimiento")
    print("   - Comparación universitarios vs no universitarios")
    
    print("\n4. Análisis por Preparación para Exámenes")
    print("   - Impacto del curso de preparación")
    print("   - Mejoras por materia")
    print("   - Análisis combinado con género")
    
    print("\n5. Análisis por Tipo de Almuerzo (Nivel Socioeconómico)")
    print("   - Comparación standard vs free/reduced")
    print("   - Brechas de rendimiento")
    print("   - Interacción con otros factores")
    
    print("\n6. Análisis por Grupo Étnico")
    print("   - Rendimiento por grupo")
    print("   - Brechas entre grupos")
    print("   - Interacciones con educación y género")
    
    print("\n7. Ejecutar TODOS los análisis")
    print("\n0. Salir")
    print("\n" + "=" * 80)

def ejecutar_programa(nombre_archivo):
    """Ejecuta un programa de análisis específico"""
    try:
        print(f"\n\nEjecutando {nombre_archivo}...")
        print("-" * 80)
        script = CARPETA_PANDAS / nombre_archivo
        resultado = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(CARPETA_PANDAS),
            capture_output=False,
            text=True,
        )
        
        if resultado.returncode == 0:
            print("\n✓ Análisis completado exitosamente")
        else:
            print("\n✗ Error al ejecutar el análisis")
            
    except Exception as e:
        print(f"\n✗ Error: {e}")

def ejecutar_todos():
    """Ejecuta todos los análisis disponibles"""
    programas = [
        ('analisis_general.py', 'Análisis General'),
        ('analisis_por_genero.py', 'Análisis por Género'),
        ('analisis_educacion_parental.py', 'Análisis por Educación Parental'),
        ('analisis_preparacion.py', 'Análisis por Preparación para Exámenes'),
        ('analisis_almuerzo.py', 'Análisis por Tipo de Almuerzo'),
        ('analisis_grupo_etnico.py', 'Análisis por Grupo Étnico')
    ]
    
    print("\n\n" + "=" * 80)
    print("EJECUTANDO TODOS LOS ANÁLISIS")
    print("=" * 80)
    
    for i, (archivo, nombre) in enumerate(programas, 1):
        print(f"\n\n[{i}/{len(programas)}] {nombre}")
        ejecutar_programa(archivo)
        
        if i < len(programas):
            input("\nPresione ENTER para continuar con el siguiente análisis...")
    
    print("\n\n" + "=" * 80)
    print("✓ TODOS LOS ANÁLISIS COMPLETADOS")
    print("=" * 80)

def main():
    """Función principal del programa"""
    
    opciones = {
        '1': ('analisis_general.py', 'Análisis General'),
        '2': ('analisis_por_genero.py', 'Análisis por Género'),
        '3': ('analisis_educacion_parental.py', 'Análisis por Educación Parental'),
        '4': ('analisis_preparacion.py', 'Análisis por Preparación para Exámenes'),
        '5': ('analisis_almuerzo.py', 'Análisis por Tipo de Almuerzo'),
        '6': ('analisis_grupo_etnico.py', 'Análisis por Grupo Étnico')
    }
    
    while True:
        mostrar_menu()
        
        opcion = input("\nIngrese su opción (0-7): ").strip()
        
        if opcion == '0':
            print("\n¡Hasta luego!")
            break
        
        elif opcion == '7':
            ejecutar_todos()
            input("\nPresione ENTER para volver al menú principal...")
        
        elif opcion in opciones:
            archivo, nombre = opciones[opcion]
            print(f"\n\n{'=' * 80}")
            print(f"EJECUTANDO: {nombre}")
            print('=' * 80)
            ejecutar_programa(archivo)
            input("\nPresione ENTER para volver al menú principal...")
        
        else:
            print("\n✗ Opción no válida. Por favor, seleccione una opción del 0 al 7.")
            input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n¡Programa interrumpido por el usuario!")
        sys.exit(0)

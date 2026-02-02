"""
Switch - Ejemplo 3: match / case (Python 3.10+)
===============================================
Tema: Condicionales - Switch (02_Condicionales)
Descripción: Sintaxis nativa match/case, similar a switch en otros lenguajes.
"""

comando = "salir"

match comando:
    case "iniciar":
        print("Iniciando...")
    case "pausar":
        print("Pausado")
    case "salir":
        print("Saliendo...")
    case _:
        print("Comando desconocido")  # _ = default

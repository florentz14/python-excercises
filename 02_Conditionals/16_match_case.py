"""
Switch - Ejemplo 3: match / case (Python 3.10+)
===============================================
Topic: Conditionals - Switch (02_Conditionals)
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

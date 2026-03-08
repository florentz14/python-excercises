# -------------------------------------------------
# File Name: 16_match_case.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Sintaxis nativa match/case, similar a switch en otros lenguajes.
# -------------------------------------------------

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

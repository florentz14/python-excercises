# -------------------------------------------------
# File Name: 108_echo_until_exit.py
# Description: Echo input until user types "salir"
# -------------------------------------------------

while True:
    line = input("> ")
    if line.lower() == "salir":
        break
    print(line)

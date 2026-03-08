# -------------------------------------------------
# File Name: 95_while_menu_loop.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Simple menu (1=hello, 2=bye, 0=exit).
# -------------------------------------------------

while True:
    print("\nMenu: 1=Hello | 2=Bye | 0=Exit")
    choice = input("Choice: ")
    if choice == "0":
        print("Goodbye!")
        break
    elif choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Bye!")
    else:
        print("Invalid option")

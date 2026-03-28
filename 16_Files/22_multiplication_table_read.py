# -------------------------------------------------
# File Name: 22_multiplication_table_read.py
# Created: 2026-03-08
# Description: Ask for integer 1-10, read table-n.txt and display it
# -------------------------------------------------


def read_multiplication_table() -> None:
    """Asks for integer 1-10, reads table-n.txt and displays it."""
    while True:
        try:
            n = int(input("Enter an integer between 1 and 10: "))
            if 1 <= n <= 10:
                break
            print("Number must be between 1 and 10.")
        except ValueError:
            print("Enter a valid integer.")

    filename = f"table-{n}.txt"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")


if __name__ == "__main__":
    read_multiplication_table()

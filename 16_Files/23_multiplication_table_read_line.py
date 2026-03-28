# -------------------------------------------------
# File Name: 23_multiplication_table_read_line.py
# Created: 2026-03-08
# Description: Ask for n and m (1-10), read line m from table-n.txt
# -------------------------------------------------


def read_table_line() -> None:
    """Asks for n and m (1-10), reads line m from table-n.txt."""
    while True:
        try:
            n = int(input("Enter n (integer 1-10): "))
            m = int(input("Enter m (integer 1-10): "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                break
            print("Both numbers must be between 1 and 10.")
        except ValueError:
            print("Enter valid integers.")

    filename = f"table-{n}.txt"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if 1 <= m <= len(lines):
                print(lines[m - 1].rstrip())
            else:
                print(f"Line {m} does not exist (table has {len(lines)} lines).")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")


if __name__ == "__main__":
    read_table_line()

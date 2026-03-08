# -------------------------------------------------
# File Name: 21_multiplication_table_save.py
# Description: Ask for integer 1-10, save multiplication table to table-n.txt
# -------------------------------------------------


def save_multiplication_table() -> None:
    """Asks for integer 1-10 and saves multiplication table to table-n.txt."""
    while True:
        try:
            n = int(input("Enter an integer between 1 and 10: "))
            if 1 <= n <= 10:
                break
            print("Number must be between 1 and 10.")
        except ValueError:
            print("Enter a valid integer.")

    filename = f"table-{n}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n * i}\n")

    print(f"Table saved to '{filename}'.")


if __name__ == "__main__":
    save_multiplication_table()

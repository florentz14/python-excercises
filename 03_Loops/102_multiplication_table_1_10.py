# -------------------------------------------------
# File Name: 102_multiplication_table_1_10.py
# Description: Multiplication table 1 to 10
# -------------------------------------------------

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()

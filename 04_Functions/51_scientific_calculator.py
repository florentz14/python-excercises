# -------------------------------------------------
# File Name: 51_scientific_calculator.py
# Description: Scientific calculator: sin, cos, tan, exp, log - table of results
# -------------------------------------------------

import math


def scientific_calculator() -> None:
    """Ask for value and function, print table 1..n with function applied."""
    funcs = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "log": math.log,
    }
    print("Available: sin, cos, tan, exp, log")
    name = input("Function: ").strip().lower()
    if name not in funcs:
        print("Unknown function.")
        return
    try:
        n = int(input("Enter integer value: "))
    except ValueError:
        print("Invalid number.")
        return

    f = funcs[name]
    print(f"\n{'x':>4} | {name}(x)")
    print("-" * 20)
    for i in range(1, n + 1):
        try:
            result = f(i)
            print(f"{i:>4} | {result:.4f}")
        except ValueError as e:
            print(f"{i:>4} | error: {e}")


if __name__ == "__main__":
    scientific_calculator()

# -------------------------------------------------
# File Name: 49_lambda_chapter_tutorial.py
# Author: Florentino Báez
# Date: 04_Functions
# Description: Simple lambda functions with one or more arguments."""
# -------------------------------------------------

def section1_basic():
    """Simple lambda functions with one or more arguments."""
    add = lambda a, b: a + b
    print(add(2, 3))
    print(add(5, 5))

    greet = lambda name: f"Hello {name}!"
    print(greet("Juan"))
    print(greet("Ana"))


# =============================================================================
# Section 2: Calling Functions Inside a Lambda
# The lambda expression can call other functions (e.g., built-ins).
# =============================================================================

def section2_inner_calls():
    """Lambda that calls max() in its expression."""
    get_max = lambda a, b, c: f"The maximum of {a}, {b}, {c} is: {max(a, b, c)}"
    print(get_max(3, 4, 5))


# =============================================================================
# Section 3: Lambda Inside Regular Functions
# Define lambdas inside functions to create specialized functions
# with different parameters (closure / factory pattern).
# =============================================================================

def add_prefix(prefix: str):
    """Return a lambda that prepends prefix to any name."""
    return lambda name: f"{prefix} {name}"


def power_of(exponent: int):
    """Return a lambda that raises a base to the given exponent."""
    return lambda base: base**exponent


def section3_factories():
    """Lambdas as factories - different functions from one definition."""
    add_mr = add_prefix("Mr")
    add_miss = add_prefix("Miss")
    add_sr = add_prefix("Sr")

    print(add_mr("Manuel"))
    print(add_miss("Nerea"))
    print(add_sr("Rodolfo"))

    square = power_of(2)
    cube = power_of(3)

    print(square(3))
    print(cube(2))


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("1. Basic Lambda - add, greet")
    print("=" * 55)
    section1_basic()

    print("\n" + "=" * 55)
    print("2. Lambda Calling Built-in (max)")
    print("=" * 55)
    section2_inner_calls()

    print("\n" + "=" * 55)
    print("3. Lambda Factories (closures)")
    print("=" * 55)
    section3_factories()

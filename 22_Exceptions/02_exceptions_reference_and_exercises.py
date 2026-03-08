# -------------------------------------------------
# File Name: 02_exceptions_reference_and_exercises.py
# Author: Florentino Báez
# Date: 22_Exceptions
# Description: Demonstrates exceptions reference and exercises.
# -------------------------------------------------

import sys

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

DIVIDEND = 150
NUMBERS = [6, 14, 11, 3, 2, 1, 15, 19]
SAMPLE_DICT = {"name": "Alice", "age": 30, "city": "Madrid"}


# -----------------------------------------------------------------------------
# try / except / finally - Division example
# -----------------------------------------------------------------------------

def divide_safe(dividend: float, divisor_str: str) -> float | None:
    """Convert divisor_str to int, divide. Returns result or None on error."""
    try:
        divisor = int(divisor_str)
        return dividend / divisor
    except ValueError:
        print("Invalid number")
        return None
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    finally:
        print("(finally block executed)")


# -----------------------------------------------------------------------------
# raise - Explicit exception
# -----------------------------------------------------------------------------

def demo_raise() -> None:
    """Show explicit raise. Uncomment the line to trigger."""
    # raise NameError("I am an exception!")
    pass


# -----------------------------------------------------------------------------
# Common Exceptions - Demo
# -----------------------------------------------------------------------------


def _trigger_type_error() -> None:
    _ = "1" + 1  # type: ignore[operator]  # Intentional: raises TypeError


def _trigger_value_error() -> None:
    int("hello")


def _trigger_name_error() -> None:
    raise NameError("name 'person' is not defined")


def _trigger_index_error() -> None:
    [1, 2, 3][5]


def _trigger_key_error():
    {"a": 1}["b"]


def demo_common_exceptions() -> None:
    """Print common exception types and their messages."""
    cases = [
        ("TypeError", _trigger_type_error),
        ("ValueError", _trigger_value_error),
        ("NameError", _trigger_name_error),
        ("IndexError", _trigger_index_error),
        ("KeyError", _trigger_key_error),
    ]
    for name, trigger in cases:
        try:
            trigger()
        except Exception as e:
            print(f"  {name}: {e}")


# -----------------------------------------------------------------------------
# Exercise 1: Access list by index (ValueError, IndexError)
# -----------------------------------------------------------------------------

def access_list_at(data: list[int], index_str: str) -> int | None:
    """Return data[index] or None. Handles ValueError, IndexError."""
    try:
        idx = int(index_str)
        return data[idx]
    except ValueError:
        print(f"Error: enter an integer between 0 and {len(data) - 1}")
        return None
    except IndexError:
        print(f"Error: index must be 0-{len(data) - 1}")
        return None


def run_exercise1_interactive() -> None:
    """Interactive: user enters index to access NUMBERS."""
    print(f"List: {NUMBERS}")
    while True:
        user_input = input("Enter index (or 'q' to quit): ").strip()
        if user_input.lower() == "q":
            break
        result = access_list_at(NUMBERS, user_input)
        if result is not None:
            print(f"Value at index {user_input}: {result}")


# -----------------------------------------------------------------------------
# Exercise 2: Access dict by key (KeyError)
# -----------------------------------------------------------------------------

def access_dict(data: dict, key: str):
    """Return data[key] or None. Handles KeyError."""
    try:
        return data[key]
    except KeyError:
        print(f"Error: key '{key}' not found. Valid keys: {list(data)}")
        return None


def run_exercise2_interactive() -> None:
    """Interactive: user enters key to access SAMPLE_DICT."""
    print(f"Dictionary: {SAMPLE_DICT}")
    while True:
        user_input = input("Enter key (or 'q' to quit): ").strip()
        if user_input.lower() == "q":
            break
        result = access_dict(SAMPLE_DICT, user_input)
        if result is not None:
            print(f"Value: {result}")


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def run_demo() -> None:
    """Non-interactive demo of all sections."""
    print("=" * 55)
    print("1. try / except / finally - Division")
    print("=" * 55)
    for inp in ("5", "abc", "0"):
        result = divide_safe(DIVIDEND, inp)
        if result is not None:
            print(result)

    print("\n" + "=" * 55)
    print("2. Common Exceptions")
    print("=" * 55)
    demo_common_exceptions()

    print("\n" + "=" * 55)
    print("3. Exercise 1: Access list by index")
    print(f"   List: {NUMBERS}")
    print("=" * 55)
    for inp in ("3", "20", "xyz"):
        result = access_list_at(NUMBERS, inp)
        if result is not None:
            print(f"   Value at {inp}: {result}")

    print("\n" + "=" * 55)
    print("4. Exercise 2: Access dict by key")
    print(f"   Dict: {SAMPLE_DICT}")
    print("=" * 55)
    for key in ("name", "country"):
        result = access_dict(SAMPLE_DICT, key)
        if result is not None:
            print(f"   Value for '{key}': {result}")


def run_interactive() -> None:
    """Interactive mode: Exercises 1 and 2 with user input."""
    print("=" * 55)
    print("Interactive Exception Exercises")
    print("=" * 55)
    while True:
        print("\n1. Access list by index")
        print("2. Access dict by key")
        print("q. Quit")
        choice = input("Choice: ").strip().lower()
        if choice == "q":
            break
        if choice == "1":
            run_exercise1_interactive()
        elif choice == "2":
            run_exercise2_interactive()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    if "-i" in sys.argv or "--interactive" in sys.argv:
        run_interactive()
    else:
        run_demo()

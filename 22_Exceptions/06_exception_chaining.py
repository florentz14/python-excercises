# -------------------------------------------------
# File Name: 06_exception_chaining.py
# Author: Florentino Báez
# Date: 22_Exceptions
# Description: Exception Chaining. load_config implementation.
# -------------------------------------------------

def load_config(path: str) -> dict:
    """
    Load config from JSON file. Raises ConfigError with original
    cause if file is missing or invalid JSON.
    """
    class ConfigError(Exception):
        """Configuration loading failed."""
        pass

    try:
        with open(path, encoding="utf-8") as f:
            import json
            return json.load(f)
    except FileNotFoundError as e:
        raise ConfigError(f"Config file not found: {path}") from e
    except json.JSONDecodeError as e:
        raise ConfigError(f"Invalid JSON in {path}") from e


def parse_user_id(value: str) -> int:
    """
    Parse user ID from string. Raises UserError with cause
    if conversion fails or ID is invalid.
    """
    class UserError(Exception):
        """User data validation failed."""
        pass

    try:
        uid = int(value)
        if uid < 1:
            raise ValueError(f"User ID must be positive, got {uid}")
        return uid
    except ValueError as e:
        raise UserError(f"Invalid user ID: {value!r}") from e


# -----------------------------------------------------------------------------
# Main - Run examples
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 55)
    print("1. ConfigError chained from FileNotFoundError")
    print("=" * 55)
    try:
        load_config("nonexistent_config.json")
    except Exception as e:
        print(f"Caught: {e}")
        print(f"Cause: {e.__cause__}")
        print(f"Traceback includes both exceptions")

    print("\n" + "=" * 55)
    print("2. UserError chained from ValueError")
    print("=" * 55)
    for val in ("123", "-5", "abc"):
        try:
            uid = parse_user_id(val)
            print(f"  '{val}' -> {uid}")
        except Exception as e:
            print(f"  '{val}' -> Error: {e}")
            if e.__cause__:
                print(f"       Cause: {e.__cause__}")

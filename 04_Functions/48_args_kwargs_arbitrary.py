# -------------------------------------------------
# File Name: 48_args_kwargs_arbitrary.py
# Author: Florentino Báez
# Date: 04_Functions
# Description: Return the maximum value among all arguments.
# -------------------------------------------------

def find_maximum(*args):
    """
    Return the maximum value among all arguments.
    Uses *args to accept any number of positional arguments.
    """
    if not args:
        return None
    # Optimized: use built-in max() instead of manual loop
    return max(args)


def format_download(media_type: str, *args) -> str:
    """
    Build a download format description based on type and optional args.
    Video: optional resolution, optional (resolution, fps).
    Audio: no extra args.
    """
    if media_type == "video":
        if len(args) == 0:
            return f"Format: {media_type}"
        if len(args) == 1:
            return f"Format: {media_type}\nResolution: {args[0]}"
        # Two args: resolution and fps
        return f"Format: {media_type}\nResolution: {args[0]}\nFPS: {args[1]}"
    if media_type == "audio":
        return f"Format: {media_type}"
    return "Error: unknown format."


# =============================================================================
# Section 2: Keyword Arguments
# Pass arguments by name; order becomes irrelevant.
# =============================================================================

def create_character(clase: str, raza: str, nombre: str) -> None:
    """Display a character description using keyword arguments."""
    print(f"{nombre} is a {clase} ({raza})")


# =============================================================================
# Section 3: Keyword Arbitrary Arguments (**kwargs)
# Use when the number of keyword arguments is unknown.
# =============================================================================

def print_attributes(**kwargs) -> None:
    """Print all key-value pairs passed as keyword arguments."""
    print("\nCharacter attributes:")
    for key, value in kwargs.items():
        print(f"  {key} --> {value}")


# =============================================================================
# Section 4: Combined Usage (*args + **kwargs)
# Both can be used together in the same function signature.
# =============================================================================

def create_character_sheet(nombre: str, *skills, **attributes) -> str:
    """
    Build a character sheet with skills (args) and attributes (kwargs).
    Skills become a bullet list; attributes become a key-value section.
    """
    sheet = f"##### {nombre.upper()} #####\n\n"
    sheet += "##### DESCRIPTION #####\n\n"
    for key, value in attributes.items():
        sheet += f"- {key} --> {value}\n"
    sheet += "\n##### SKILLS #####\n\n"
    for skill in skills:
        sheet += f"- {skill}\n"
    return sheet


# =============================================================================
# Main - Run all examples
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("1. Arbitrary Arguments (*args)")
    print("=" * 55)
    print("Maximum of (0, 90, 23, 11, 10, -5):")
    print(find_maximum(0, 90, 23, 11, 10, -5))
    print("\nMaximum of (0, 110, 23, 110.45, 10.23, -10, 33, 55):")
    print(find_maximum(0, 110, 23, 110.45, 10.23, -10, 33, 55))

    print("\n" + "=" * 55)
    print("Format download examples:")
    print("=" * 55)
    print(format_download("audio"))
    print()
    print(format_download("video", 720))
    print()
    print(format_download("video", 1080, 60))

    print("\n" + "=" * 55)
    print("2. Keyword Arguments")
    print("=" * 55)
    create_character(clase="mage", nombre="Thorofin", raza="Elf")
    create_character(nombre="Askland", clase="Rogue", raza="Human")

    print("\n" + "=" * 55)
    print("3. Keyword Arbitrary Arguments (**kwargs)")
    print("=" * 55)
    print_attributes(clase="mage", nombre="Thorofin", raza="Elf")
    print_attributes(
        clase="mage",
        nombre="Thorofin",
        raza="Elf",
        mascota="Dragon",
        nivel="165",
        clan="ValenciaFC",
    )

    print("\n" + "=" * 55)
    print("4. Combined (*args + **kwargs)")
    print("=" * 55)
    character = create_character_sheet(
        "Dandelion",
        "strong attack",
        "dodge",
        "smoke bomb",
        raza="Elf",
        mascota="Dragon",
        nivel="165",
        clan="ValenciaFC",
    )
    print(character)

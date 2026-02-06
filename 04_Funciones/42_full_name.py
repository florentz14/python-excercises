# 42_full_name.py
# Function to combine first and last name into full name

def full_name(first_name, last_name):
    """
    Combines first and last name into a full name.
    
    Args:
        first_name: The person's first name
        last_name: The person's last name
        
    Returns:
        Full name as a single string
    """
    return f"{first_name} {last_name}"


def full_name_formatted(first_name, last_name, uppercase=False):
    """
    Combines names with optional formatting.
    
    Args:
        first_name: The person's first name
        last_name: The person's last name
        uppercase: If True, returns name in uppercase
        
    Returns:
        Formatted full name
    """
    name = f"{first_name} {last_name}"
    return name.upper() if uppercase else name.title()


def full_name_with_middle(first_name, *middle_names, last_name):
    """
    Combines first, middle, and last names.
    
    Args:
        first_name: The person's first name
        *middle_names: Optional middle names
        last_name: The person's last name (keyword argument)
        
    Returns:
        Full name including middle names
    """
    if middle_names:
        middle = " ".join(middle_names)
        return f"{first_name} {middle} {last_name}"
    return f"{first_name} {last_name}"


def parse_full_name(full_name_str):
    """
    Parses a full name string into components.
    
    Args:
        full_name_str: Full name as a string
        
    Returns:
        Dictionary with first_name, middle_names, last_name
    """
    parts = full_name_str.strip().split()
    if len(parts) == 1:
        return {'first_name': parts[0], 'middle_names': [], 'last_name': ''}
    elif len(parts) == 2:
        return {'first_name': parts[0], 'middle_names': [], 'last_name': parts[1]}
    else:
        return {
            'first_name': parts[0],
            'middle_names': parts[1:-1],
            'last_name': parts[-1]
        }


# Example usage
if __name__ == "__main__":
    print("=== Full Name Function Demo ===\n")
    
    # Basic full name
    print("1. Basic full_name():")
    print(f"   full_name('John', 'Doe') = '{full_name('John', 'Doe')}'")
    print(f"   full_name('Maria', 'Garcia') = '{full_name('Maria', 'Garcia')}'")
    
    print()
    
    # Formatted full name
    print("2. full_name_formatted():")
    print(f"   Normal: '{full_name_formatted('john', 'doe')}'")
    print(f"   Uppercase: '{full_name_formatted('john', 'doe', uppercase=True)}'")
    
    print()
    
    # With middle names
    print("3. full_name_with_middle():")
    print(f"   '{full_name_with_middle('John', last_name='Doe')}'")
    print(f"   '{full_name_with_middle('John', 'William', last_name='Doe')}'")
    print(f"   '{full_name_with_middle('Maria', 'Isabel', 'Rosa', last_name='Garcia')}'")
    
    print()
    
    # Parse full name
    print("4. parse_full_name():")
    names = ["John Doe", "Maria Isabel Garcia", "Prince"]
    for name in names:
        parsed = parse_full_name(name)
        print(f"   '{name}' -> {parsed}")

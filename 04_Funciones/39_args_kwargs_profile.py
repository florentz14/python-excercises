# 39_args_kwargs_profile.py
# Function with *args and **kwargs - flexible arguments

def create_profile(name, *hobbies, **details):
    """
    Creates a user profile with flexible parameters.
    
    Args:
        name: Required - the user's name
        *hobbies: Variable positional args - list of hobbies
        **details: Variable keyword args - additional details
        
    Returns:
        Dictionary containing the complete profile
    """
    profile = {'name': name, 'hobbies': list(hobbies)}
    profile.update(details)
    return profile


def format_message(template, *args, **kwargs):
    """
    Formats a message using positional and keyword arguments.
    
    Args:
        template: String template with {} placeholders
        *args: Positional values to insert
        **kwargs: Named values to insert
        
    Returns:
        Formatted string
    """
    # First replace positional args
    for arg in args:
        template = template.replace('{}', str(arg), 1)
    # Then replace named args
    for key, value in kwargs.items():
        template = template.replace(f'{{{key}}}', str(value))
    return template


def sum_all(*numbers, initial=0):
    """
    Sums all provided numbers with an optional initial value.
    
    Args:
        *numbers: Variable number of values to sum
        initial: Starting value (default 0)
        
    Returns:
        Sum of all numbers plus initial
    """
    return initial + sum(numbers)


# Example usage
if __name__ == "__main__":
    print("=== *args and **kwargs Demo ===\n")
    
    # Example 1: Create profile
    print("1. Creating user profiles:")
    
    profile1 = create_profile("Alice")
    print(f"   Basic: {profile1}")
    
    profile2 = create_profile("Bob", "reading", "gaming")
    print(f"   With hobbies: {profile2}")
    
    profile3 = create_profile(
        "Charlie",
        "coding", "hiking", "music",
        age=28,
        city="New York",
        email="charlie@email.com"
    )
    print(f"   Full profile: {profile3}")
    
    print()
    
    # Example 2: Format message
    print("2. Formatting messages:")
    msg1 = format_message("Hello, {}!", "World")
    print(f"   {msg1}")
    
    msg2 = format_message("User {name} is {age} years old", name="Alice", age=25)
    print(f"   {msg2}")
    
    print()
    
    # Example 3: Sum all
    print("3. Summing numbers:")
    print(f"   sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
    print(f"   sum_all(1, 2, 3, initial=10) = {sum_all(1, 2, 3, initial=10)}")
    print(f"   sum_all(10, 20, 30, 40, 50) = {sum_all(10, 20, 30, 40, 50)}")

# -------------------------------------------------
# File Name: 42_safe_nested.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Safe access to nested dicts with get() chain and helper.
# -------------------------------------------------

nested = {'user': {'profile': {'name': 'Alice', 'age': 30}}}

try:
    name = nested['user']['profile']['name']
    print("Name:", name)
except KeyError as e:
    print("KeyError:", e)

# Safe access with get()
name_safe = nested.get('user', {}).get('profile', {}).get('name', 'Unknown')
print("Safe name:", name_safe)

# Missing key
missing = nested.get('user', {}).get(
    'profile', {}).get('email', 'Not provided')
print("Missing email:", missing)

# Using a helper function


def safe_get(dct, keys, default=None):
    """Safely get nested dictionary value."""
    for key in keys:
        if isinstance(dct, dict) and key in dct:
            dct = dct[key]
        else:
            return default
    return dct


name_helper = safe_get(nested, ['user', 'profile', 'name'])
print("Using helper:", name_helper)

email_helper = safe_get(nested, ['user', 'profile', 'email'], 'No email')
print("Missing with helper:", email_helper)

# Python 3.10+ structural pattern matching (advanced)
# Not shown here as it requires newer Python

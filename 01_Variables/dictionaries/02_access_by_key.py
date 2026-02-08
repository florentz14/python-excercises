# -------------------------------------------------
# File Name: 02_access_by_key.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Access Dictionary Values by Key.
#              Shows how to retrieve values using bracket
#              notation dict[key]. Raises KeyError if the
#              key does not exist in the dictionary.
# -------------------------------------------------

# Example 2: Access dictionary values by key
print("Example 2: Access dictionary values by key")
print("-" * 40)

# Dictionary with personal information
person = {"name": "Alice", "age": 25,
          "city": "New York", "profession": "Engineer"}

print("Dictionary:", person)
print("Name:", person["name"])          # Access value using key
print("Age:", person["age"])            # Returns the value mapped to "age"
print("City:", person["city"])          # Direct key access is O(1)

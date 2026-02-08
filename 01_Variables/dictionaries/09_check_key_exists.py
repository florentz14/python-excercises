# Example 9: Check if key exists
print("Example 9: Check if key exists")
print("-" * 40)
settings = {"theme": "dark", "language": "English", "notifications": True}
print("Dictionary:", settings)
if "theme" in settings:
    print("'theme' is in the dictionary")
if "password" not in settings:
    print("'password' is not in the dictionary")

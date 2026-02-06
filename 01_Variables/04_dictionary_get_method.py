# Example 3: Use get() method
print("Example 3: Use get() method")
print("-" * 40)
user = {"username": "johndoe", "email": "john@example.com", "active": True}
print("Dictionary:", user)
print("Username:", user.get("username"))
print("Phone (not exists):", user.get("phone", "Not provided"))

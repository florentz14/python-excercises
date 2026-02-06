# 38_validate_user_password.py
# Functions to validate username and password

def validate_username(username):
    """
    Validates username format.
    
    Rules:
        - Must be 3-20 characters long
        - Can only contain letters, numbers, and underscores
        - Cannot start with a number
        
    Args:
        username: String to validate
        
    Returns:
        Tuple (is_valid, message)
    """
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    if len(username) > 20:
        return False, "Username cannot exceed 20 characters"
    if username[0].isdigit():
        return False, "Username cannot start with a number"
    
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
    for char in username:
        if char not in allowed_chars:
            return False, f"Invalid character '{char}'. Only letters, numbers, and underscore allowed"
    
    return True, "Valid username"


def validate_password(password):
    """
    Validates password strength.
    
    Rules:
        - Must be at least 8 characters long
        - Must contain at least one uppercase letter
        - Must contain at least one lowercase letter
        - Must contain at least one digit
        - Must contain at least one special character
        
    Args:
        password: String to validate
        
    Returns:
        Tuple (is_valid, message)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    if not has_lower:
        return False, "Password must contain at least one lowercase letter"
    if not has_digit:
        return False, "Password must contain at least one digit"
    if not has_special:
        return False, "Password must contain at least one special character"
    
    return True, "Strong password"


def get_password_strength(password):
    """
    Returns password strength score (0-5).
    
    Args:
        password: String to evaluate
        
    Returns:
        Tuple (score, strength_label)
    """
    score = 0
    
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
    
    labels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong",
        6: "Excellent"
    }
    
    return score, labels[score]


def login(username, password, users_db):
    """
    Validates login credentials against a user database.
    
    Args:
        username: Username to check
        password: Password to verify
        users_db: Dictionary with username:password pairs
        
    Returns:
        Tuple (success, message)
    """
    if username not in users_db:
        return False, "Username not found"
    if users_db[username] != password:
        return False, "Incorrect password"
    return True, "Login successful"


# Example usage
if __name__ == "__main__":
    print("=== User & Password Validation Demo ===\n")
    
    # Test usernames
    print("1. Username Validation:")
    test_usernames = ["john_doe", "ab", "123user", "valid_user123", "user@name"]
    for username in test_usernames:
        valid, msg = validate_username(username)
        status = "OK" if valid else "FAIL"
        print(f"   '{username}' -> [{status}] {msg}")
    
    print()
    
    # Test passwords
    print("2. Password Validation:")
    test_passwords = ["weak", "NoDigits!", "nospecial1", "Short1!", "Strong@Pass123"]
    for pwd in test_passwords:
        valid, msg = validate_password(pwd)
        status = "OK" if valid else "FAIL"
        print(f"   '{pwd}' -> [{status}] {msg}")
    
    print()
    
    # Password strength
    print("3. Password Strength:")
    for pwd in ["123456", "password", "Pass123", "Str0ng!", "Super@Secure123"]:
        score, label = get_password_strength(pwd)
        print(f"   '{pwd}' -> Score: {score}/6 ({label})")
    
    print()
    
    # Login simulation
    print("4. Login Simulation:")
    users = {"admin": "Admin@123", "user1": "User1Pass!"}
    
    login_attempts = [
        ("admin", "Admin@123"),
        ("admin", "wrongpass"),
        ("unknown", "password"),
        ("user1", "User1Pass!")
    ]
    
    for user, pwd in login_attempts:
        success, msg = login(user, pwd, users)
        status = "SUCCESS" if success else "FAILED"
        print(f"   Login({user}, {pwd}) -> [{status}] {msg}")

# 35_validate_email.py
# Function to validate email format

def is_valid_email(email):
    """
    Basic email validation using simple rules.
    
    Args:
        email: String to validate as email
        
    Returns:
        True if email format is valid, False otherwise
        
    Rules:
        - Must contain exactly one '@' symbol
        - Must have characters before '@' (local part)
        - Must have characters after '@' (domain part)
        - Domain must contain at least one '.'
    """
    if '@' not in email or email.count('@') != 1:
        return False
    local, domain = email.split('@')
    if not local or not domain:
        return False
    if '.' not in domain:
        return False
    return True


def validate_email_detailed(email):
    """
    Validates email and returns detailed error message.
    
    Args:
        email: String to validate
        
    Returns:
        Tuple (is_valid, message)
    """
    if '@' not in email:
        return False, "Missing '@' symbol"
    if email.count('@') > 1:
        return False, "Multiple '@' symbols found"
    
    local, domain = email.split('@')
    
    if not local:
        return False, "Empty local part (before @)"
    if not domain:
        return False, "Empty domain part (after @)"
    if '.' not in domain:
        return False, "Domain must contain '.'"
    if domain.startswith('.') or domain.endswith('.'):
        return False, "Domain cannot start or end with '.'"
    
    return True, "Valid email format"


# Example usage
if __name__ == "__main__":
    print("=== Email Validation Demo ===\n")
    
    # Test emails
    test_emails = [
        "user@example.com",
        "john.doe@company.org",
        "invalid-email",
        "missing@domain",
        "@nodomain.com",
        "noat.symbol.com",
        "double@@at.com",
        "valid@sub.domain.com"
    ]
    
    print("Simple validation:")
    for email in test_emails:
        result = "VALID" if is_valid_email(email) else "INVALID"
        print(f"  {email:30} -> {result}")
    
    print("\nDetailed validation:")
    for email in test_emails:
        valid, message = validate_email_detailed(email)
        print(f"  {email:30} -> {message}")

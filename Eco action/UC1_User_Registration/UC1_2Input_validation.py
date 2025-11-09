"""
IC1_2: Input Validation for User Registration
This module validates user input such as username, email, and password.
"""

def validate_registration_input(username: str, email: str, password: str, confirm_password: str) -> bool:
    """
    Placeholder function to validate registration input.
    Returns True if input passes basic checks, False otherwise.
    """
    if not username or not email or not password:
        print("[IC1_2] Missing required fields")
        return False
    if password != confirm_password:
        print("[IC1_2] Passwords do not match")
        return False
    print("[IC1_2] Input validation passed")
    return True

# Example usage
if __name__ == "__main__":
    validate_registration_input("testuser", "test@example.com", "pass123", "pass123")

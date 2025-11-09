"""
UC1: User Registration
Handles creation of new user accounts.
This is a placeholder module
"""

class UserRegistration:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def register(self):
        print(f"[UC1] Registering user: {self.username} with email: {self.email}")
        # In real code, this would save the user to the database
        return True

# Example usage
if __name__ == "__main__":
    dummy_user = UserRegistration("testuser", "test@example.com", "password123")
    dummy_user.register()

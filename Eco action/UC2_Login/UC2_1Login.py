"""
UC2: User Login
Handles authentication of users.
"""

class UserLogin:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def login(self):
        """
        Placeholder method to simulate user login.
        """
        print(f"[UC2] Logging in user: {self.username}")
        # In real code, this would check the username and password in the database
        if self.username == "testuser" and self.password == "password123":
            print("[UC2] Login successful")
            return True
        else:
            print("[UC2] Login failed")
            return False

# Example usage
if __name__ == "__main__":
    dummy_login = UserLogin("testuser", "password123")
    dummy_login.login()

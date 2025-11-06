"""
Handles secure login authentication.
"""

class LoginSystem:
    def __init__(self):
        # Example stored users
        self.users = {"Abigail": "green123"}

    def login(self, username, password):
        if username not in self.users:
            return "User not found."
        if self.users[username] != password:
            return "Incorrect password."
        return f"✅ Login successful! Welcome back, {username} 💚"

if __name__ == "__main__":
    login = LoginSystem()
    print(login.login("name", "pass"))

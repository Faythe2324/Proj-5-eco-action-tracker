"""
Handles user account creation for Eco Action Tracker.
"""

class UserRegistration:
    def __init__(self):
        # Temporary in-memory user list
        self.users = {}

    def create_account(self, username, email, password, confirm_password):
        if username in self.users:
            return "Username already exists."

        self.users[username] = {
            "email": email,
            "password": password,
            "eco_points": 0,
            "carbon_saved": 0.0,
            "rank": None
        }
        return f"✅ Account created successfully! Welcome, {username} 🌿"

if __name__ == "__main__":
    reg = UserRegistration()
    print(reg.create_account("name", "email", "pass", "pass"))

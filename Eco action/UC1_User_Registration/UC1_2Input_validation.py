"""
Validates registration fields before account creation.
"""

class InputValidator:
    def validate(self, username, email, password, confirm_password):
        if len(username) < 3:
            return "Username must have at least 3 characters."
        if len(password) < 6:
            return "Password must be at least 6 characters."
        if password != confirm_password:
            return "Passwords must match."
        return "Input valid."

if __name__ == "__main__":
    v = InputValidator()
    print(v.validate("Abi", "abi@mail.com", "123456", "123456"))

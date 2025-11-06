"""
Logs eco-friendly actions for the user.
"""

class EcoActionLogger:
    def __init__(self):
        self.history = []

    def log(self, username, action):
        entry = f"{username} completed: {action}"
        self.history.append(entry)
        print(f"📝 Action logged: {entry}")


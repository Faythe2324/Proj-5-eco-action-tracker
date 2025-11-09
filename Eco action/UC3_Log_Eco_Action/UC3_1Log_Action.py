"""
UC3.1: Log Eco Action
Handles recording a user's eco-friendly actions.
"""

class LogAction:
    def __init__(self, user: str, action_name: str, co2_saved: float):
        self.user = user
        self.action_name = action_name
        self.co2_saved = co2_saved

    def log(self):
        print(f"[UC3.1] {self.user} performed action: {self.action_name}, CO2 saved: {self.co2_saved} kg")
        return True

# Example usage
if __name__ == "__main__":
    dummy_action = LogAction("testuser", "Bike to Work", 2.5)
    dummy_action.log()

"""
UC7.1: Environmental API
Simulates fetching carbon saved or environmental impact data.
"""

class EnvironmentalAPI:
    def __init__(self, user: str):
        self.user = user
        # Example data for CO2 saved
        self.co2_saved_history = [2.5, 5.0, 7.2, 10.1]

    def get_total_co2_saved(self):
        """
        Placeholder method to simulate retrieving total CO2 saved by the user.
        """
        total = sum(self.co2_saved_history)
        print(f"[UC7.1] Total CO₂ saved by {self.user}: {total} kg")
        return total

    def get_history(self):
        print(f"[UC7.1] CO₂ saved history for {self.user}: {self.co2_saved_history}")
        return self.co2_saved_history

# Example usage
if __name__ == "__main__":
    api = EnvironmentalAPI("CurrentUser")
    api.get_total_co2_saved()
    api.get_history()

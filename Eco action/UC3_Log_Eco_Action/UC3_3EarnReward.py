"""
UC4.1: Display Dashboard
Displays user's personal statistics like points, rank, and CO2 saved.
"""

class DisplayDashboard:
    def __init__(self, user: str):
        self.user = user

    def show(self):
        print(f"[UC4.1] Dashboard for {self.user}")
        print("Points: 120")
        print("Rank: #3")
        print("CO2 Saved: 12.5 kg")
        return True

# Example usage
if __name__ == "__main__":
    dashboard = DisplayDashboard("testuser")
    dashboard.show()

"""
UC4.2: Progress Summary
Provides a summary of the user's eco action progress over time.
"""

class ProgressSummary:
    def __init__(self, user: str):
        self.user = user

    def summary(self):
        co2_history = [2.5, 3.0, 4.0, 2.0]
        points_history = [25, 30, 40, 20]
        print(f"[UC4.2] Progress Summary for {self.user}")
        for i, (pts, co2) in enumerate(zip(points_history, co2_history), 1):
            print(f"Action {i}: {pts} pts, {co2} kg CO2 saved")
        return True

# Example usage
if __name__ == "__main__":
    progress = ProgressSummary("testuser")
    progress.summary()

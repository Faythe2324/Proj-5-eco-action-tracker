"""
UC3.2: Score Eco Action
Calculates points for eco actions.
"""

class ScoreEcoAction:
    def __init__(self, action_name: str):
        self.action_name = action_name

    def calculate_points(self):
        points_table = {
            "Bike to Work": 25,
            "Recycling": 15,
            "Energy Save": 20
        }
        points = points_table.get(self.action_name, 10)
        print(f"[UC3.2] Action: {self.action_name} scored {points} points")
        return points

# Example usage
if __name__ == "__main__":
    scorer = ScoreEcoAction("Bike to Work")
    scorer.calculate_points()

"""
UC5.1: Challenge List
Displays a list of available community challenges.
"""

class ChallengeList:
    def __init__(self):
        self.challenges = [
            {"name": "Zero Waste Week", "reward_points": 100},
            {"name": "Bike 50km Challenge", "reward_points": 250},
            {"name": "Plant 5 Trees Challenge", "reward_points": 50}
        ]

    def display(self):
        print("[UC5.1] Available Community Challenges:")
        for idx, ch in enumerate(self.challenges, 1):
            print(f"{idx}. {ch['name']} (+{ch['reward_points']} pts)")
        return True

# Example usage
if __name__ == "__main__":
    clist = ChallengeList()
    clist.display()

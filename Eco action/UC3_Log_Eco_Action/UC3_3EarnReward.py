"""
UC3.3: Earn Reward
Handles reward allocation after logging an eco action.
"""

class EarnReward:
    def __init__(self, user: str, points: int):
        self.user = user
        self.points = points

    def award(self):
        print(f"[UC3.3] {self.user} earned {self.points} points for eco actions")
        return True

# Example usage
if __name__ == "__main__":
    reward = EarnReward("testuser", 25)
    reward.award()

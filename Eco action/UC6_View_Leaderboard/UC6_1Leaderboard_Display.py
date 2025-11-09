"""
UC6.1: Leaderboard Display
Displays the ranking of users based on points earned.
"""

class LeaderboardDisplay:
    def __init__(self):
        # Example leaderboard data
        self.leaderboard = [
            {"username": "UserA", "points": 2100},
            {"username": "UserB", "points": 1800},
            {"username": "UserC", "points": 1100},
            {"username": "CurrentUser", "points": 1500}
        ]

    def show(self):
        print("[UC6.1] Leaderboard Rankings:")
        sorted_board = sorted(self.leaderboard, key=lambda x: x["points"], reverse=True)
        for rank, user in enumerate(sorted_board, 1):
            print(f"{rank}. {user['username']} - {user['points']} pts")
        return True

# Example usage
if __name__ == "__main__":
    leaderboard = LeaderboardDisplay()
    leaderboard.show()

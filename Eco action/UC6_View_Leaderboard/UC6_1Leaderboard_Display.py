class Leaderboard:
    def display(self, scores):
        sorted_scores = sorted(scores.items(), key=lambda x: -x[1])
        print("\n🌟 Leaderboard 🌟")
        rank = 1
        for user, pts in sorted_scores:
            print(f"{rank}. {user} — {pts} pts")
            rank += 1

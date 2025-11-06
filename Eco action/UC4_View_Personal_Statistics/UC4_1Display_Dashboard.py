class Dashboard:
    def show(self, username, points, rank, carbon_saved):
        print("\n🌍 ECO ACTION TRACKER")
        print(f"User: {username}")
        print(f"🥇 Points: {points} pts")
        print(f"📊 Rank: #{rank}")
        print(f"🌫️ CO₂ Saved: {carbon_saved} kg\n")

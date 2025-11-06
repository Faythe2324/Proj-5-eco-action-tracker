class ProgressSummary:
    def show(self, progress_list):
        print("📈 Weekly Eco Progress:")
        for day, pts in progress_list.items():
            print(f"• {day}: {pts} pts")

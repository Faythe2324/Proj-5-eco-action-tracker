"""
UC5.2: Join Challenge
Handles joining a community challenge.
"""

class JoinChallenge:
    def __init__(self, user: str):
        self.user = user

    def join(self, challenge_name: str):
        print(f"[UC5.2] {self.user} joined the challenge: {challenge_name}")
        print(f"Reward points will be applied to {self.user}'s account")
        return True

# Example usage
if __name__ == "__main__":
    joiner = JoinChallenge("testuser")
    joiner.join("Zero Waste Week")

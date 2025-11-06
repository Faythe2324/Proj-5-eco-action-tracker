"""
Awards points for actions (same as UI quick actions).
"""

class EcoActionScorer:
    ACTION_POINTS = {
        "Bike to Work": 25,
        "Recycling": 15,
        "Energy Save": 20,
        "Walk": 10,
        "Public Transport": 15
    }

    def get_points(self, action):
        return self.ACTION_POINTS.get(action, 1)

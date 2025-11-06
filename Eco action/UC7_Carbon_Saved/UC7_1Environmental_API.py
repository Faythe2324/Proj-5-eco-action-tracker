import random

class CarbonAPI:
    def calculate(self, action):
        carbon_map = {
            "Bike to Work": (1.0, 3.5),
            "Recycling": (0.1, 0.5),
            "Energy Save": (0.05, 0.2),
            "Walk": (0.3, 1.0),
            "Public Transport": (0.5, 2.0)
        }
        low, high = carbon_map.get(action, (0.1, 0.3))
        return round(random.uniform(low, high), 2)

# planets.py

class Planet:
    def __init__(self, name, planet_type, size):
        self.name = name
        self.planet_type = planet_type
        self.size = size
        self.zones = []
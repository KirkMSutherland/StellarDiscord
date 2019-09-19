# player.py

from ships import ship_types

class Player:
    def __init__(self, player_name):
        self.planets = []
        self.ships = []
        self.resources = 5
        self.name = player_name

    def shipyard_build(self, type='CV'):
        if self.resources < ship_types[type]:
            return 'You require more minerals'
        else:
            self.resources = self.resources - ship_types[type]

        self.ships.append(type)
        return 'You built a {0}'.format(type)

    def get_fleet(self):
        return self.ships

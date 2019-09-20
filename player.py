# player.py

from ships import ship_types
from zones import zone_types
from planets import Planet

class Player:
    def __init__(self, player_name):
        self.planets = {}
        self.ships = []
        self.resources = 20
        self.name = player_name

    def shipyard_build(self, type='CV'):
        if type in ship_types:
            if self.resources < ship_types[type]:
                return ' requires more minerals'
            else:
                self.resources = self.resources - ship_types[type]

            self.ships.append(type)
            return ' built a {0} :rocket: , costing him {1} materials, leaving you with {2}.'.format(
                type, ship_types[type], self.resources)
        else:
            return ' tried building a ship that doesn\'t exist'

    def get_fleet(self):
        return self.ships

    def build_zone(self, planet, type):
        if type in zone_types:
            if self.resources < zone_types[type][0]:
                return ' requires more minerals'
            elif self.planets[planet].size <= len(self.planets[planet].zones):
                return ' planet {0} is already fully developped.'.format(planet)
            else:
                self.resources = self.resources - zone_types[type][0]

            self.planets[planet].zones.append(type)
            return ' built a {0} {1} , costing him {2} materials, leaving you with {3}.'.format(
                type, zone_types[type][1], zone_types[type][0], self.resources)
        else:
            return ' tried building a ship that doesn\'t exist'

    def get_zones(self, planet):
        return self.planets

    def claim_planet(self, planet):
        self.planets[planet] = Planet(planet, 'Eden', 3)
        return ' Found {0}'.format(planet)

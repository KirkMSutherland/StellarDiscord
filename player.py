# player.py

from ships import ship_types
from zones import zone_types, Zone
from resources import resource_types, Resource
from planets import Planet

class Player:
    def __init__(self, player_name):
        self.planets = {}
        self.ships = []
        self.resources = {
            'materials': Resource('materials', 50), 'cybernetics': Resource('cybernetics', 10),
            'food': Resource('food', 25)}
        self.name = player_name

    def check_costs(self, cost):
        for res in cost:
            if res not in self.resources:
                return (False, ' requires {0}'.format(cost))
            if self.resources[res].amount < cost[res]:
                return (False,' requires more {0}'.format(res))

        return (True, '')

    def consume_costs(self, cost):
        msg = ' used '
        for res in cost:
            self.resources[res].amount = self.resources[res].amount - cost[res]
            msg = msg + str(cost[res]) + self.resources[res].icon

        return msg

    def gain_costs(self, cost):
        msg = ''
        for res in cost:
            if res not in self.resources:
                self.resources[res] = {res : Resource(res, cost[res])}
            else:
                self.resources[res].amount = self.resources[res].amount + cost[res]

            msg = msg + str(cost[res]) + resource_types[res][1]
        return msg


    def shipyard_build(self, ship_type):
        if ship_type in ship_types:

            (check, msg) = self.check_costs(ship_types[ship_type])

            if check is False:
                return msg
            else:
                msg = msg + self.consume_costs(ship_types[ship_type])

            self.ships.append(ship_type)
            return msg + ' and built a {0} :rocket:'.format(
                ship_type)
        else:
            return ' tried building a ship that doesn\'t exist'

    def get_fleet(self):
        msg = '\t'.join(self.ships)
        return msg

    def build_zone(self, planet, z_type):
        if z_type in zone_types:

            if self.planets[planet].size <= len(self.planets[planet].zones):
                return ' planet {0} is already fully developped.'.format(planet)
            (check, msg) = self.check_costs(zone_types[z_type][0])

            if check is False:
                return msg
            else:
                msg = msg + self.consume_costs(zone_types[z_type][0])

            self.planets[planet].zones.append(Zone(z_type))
            return msg + ' and built a {0} {1}'.format(
                z_type, zone_types[z_type][1], )
        else:
            return ' tried building a zone that doesn\'t exist'

    def get_zones(self, planet):
        msg = '{0} is of size {1} and type {2} \n'.format(
            self.planets[planet].name, self.planets[planet].size, self.planets[planet].planet_type)
        for n in self.planets[planet].zones:
            msg = msg + n.name + n.icon + '\t'
        return msg

    def claim_planet(self, planet):
        self.planets[planet] = Planet(planet, 'Eden', 3)
        return ' Found {0}'.format(planet)

    def get_planets(self):
        msg = '\t'.join(self.planets)
        return msg

    def get_resources(self):
        msg = ''
        for n in self.resources:
            msg = msg + n + '[' + self.resources[n].icon + ']: ' + str(self.resources[n].amount) + '\t'
        return msg

    def produce(self, planet):
        for z in self.planets[planet].zones:
            (check, msg) = self.check_costs(z.input)

            if not check:
                msg = '{0} cannot produce, missing: '.format(planet) + msg
            else:
                msg = self.consume_costs(z.input)
                msg = msg + self.gain_costs(z.output)

        return msg



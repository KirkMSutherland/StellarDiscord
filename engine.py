# engine.py

import random
from player import Player
from trade import Trade

class Game:
    def __init__(self, size=10):
        self.size = size
        self.players = {}
        self.trades = {}

    def register_player(self, player_name):
        self.players[player_name] = Player(player_name)

    def get_players(self):
        return list(self.players.keys())

    def get_resources(self, player_name):
        return self.players[player_name].resources

    def build_ship(self, player_name, ship_type):
        return self.players[player_name].shipyard_build(ship_type)

    def get_fleet(self, player_name):
        return self.players[player_name].get_fleet()

    def build_zone(self, player_name, planet, zone_type):
        return self.players[player_name].build_zone(planet, zone_type)

    def claim_planet(self, player_name, planet_name):
        return self.players[player_name].claim_planet(planet_name)

    def produce(self, player_name, planet_name):
        return self.players[player_name].produce(planet_name)

    def empire(self, player_name):
        msg = ''
        msg = msg + 'Fleet: '+ self.players[player_name].get_fleet() + '\n'
        msg = msg + 'Planets: ' + self.players[player_name].get_planets() + '\n'
        msg = msg + 'Resources: ' + self.players[player_name].get_resources() + '\n'
        return msg

    def get_zones(self, player_name, planet):
        return self.players[player_name].get_zones(planet)

    def propose_trade(self, player_name, partner, args):
        if args[0] in self.trades:
            return False

        offer_list = args[2:args.index('want')]
        want_list = args[args.index('want')+1:]

        offer_dict = {}
        want_dict = {}

        for x in range(0, len(offer_list), 2):
            offer_dict[offer_list[x]] = int(offer_list[x+1])

        for x in range(0, len(want_list), 2):
            want_dict[want_list[x]] = int(want_list[x+1])

        self.trades[args[0]] = Trade(player_name.id, partner, offer_dict, want_dict)

        msg = '{0} wants to trade with '.format(player_name.mention) + '<@' + str(self.trades[args[0]].partner) + '>\n'
        msg = msg + 'Contract: ' + args[0] + '\n'
        msg = msg + 'Offers: ' + str(self.trades[args[0]].offers) + '\n'
        msg = msg + 'Wants: ' + str(self.trades[args[0]].wants)
        return msg

    def add_tradeid(self, tradename, tradeid):
        self.trades[tradename].msgid = tradeid

    def complete_trade(self, tradeid):
        trade = self.trades[tradeid]
        (check1, msg1) = self.players[trade.proposer].check_costs(trade.offers)
        (check2, msg2) = self.players[trade.partner].check_costs(trade.wants)

        if check1 and check2:
            self.players[trade.proposer].consume_costs(trade.offers)
            self.players[trade.partner].consume_costs(trade.wants)

            self.players[trade.proposer].gain_costs(trade.wants)
            self.players[trade.partner].gain_costs(trade.offers)
            return 'Trade Complete'
        else:
            return 'Trade Failed due to insufficient resources'



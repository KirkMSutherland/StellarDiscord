# engine.py

import random
from player import Player

class Game:
    def __init__(self, size=10):
        self.size = size

        self.players = {}


    def register_player(self, player_name):
        self.players[player_name] = Player(player_name)

    def get_players(self):
        return list(self.players.keys())

    def get_resources(self, player_name):
        return self.players[player_name].resources

    def build_ship(self, player_name, type):
        return self.players[player_name].shipyard_build(type)

    def get_fleet(self, player_name):
        return self.players[player_name].get_fleet()

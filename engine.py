# engine.py

import random
from player import Player

class Game:
    def __init__(self, size=10):
        self.size = size

        self.players = {}


    def register_player(self, player_name):
        self.players.append(Player(player_name))

    def get_players(self):
        list = 'Players: '
        for n in self.players:
            list = list + n.name + ', '

        return list

#    def get_fleet(self, player_name):
#        self.players.
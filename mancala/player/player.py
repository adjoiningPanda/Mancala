__author__ = 'robby'

class Player(object):
    def __init__(self, player):
        self.player = int(player)
        self.type = 'player'

    def __str__(self):
        return "Player {0}'s ({1}) turn".format(self.player, self.type)
__author__ = 'robby'

import player

#class

class ComputerPlayer(player.Player):
    def __init__(self, player, plys=3, move_automatically=False):
        super(ComputerPlayer, self).__init__(player)
        self.plys = plys
        self.move_automatically = move_automatically

    def take_turn(self, board):
        print
        if not self.move_automatically:
            raw_input("Press ENTER  to continue")

        return self._take_turn(board)

    def _take_turn(self, board):
        raise NotImplementedError("Must implement _take_turn in subclass")
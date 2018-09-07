from .board import Board
from .player import Player
from .strategy import BasicStrategy


class Game:

    def __init__(self, board):
        self.board = board
        self.players = board.players

    def play(self):
        while True:
            for player in self.players:
                player.play()


if __name__ == '__main__':
    players = [Player(BasicStrategy()) for i in range(4)]
    board = Board('boards/uk_london', players)
    game = Game(board)
    game.play()

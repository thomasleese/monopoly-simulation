from .board import Board
from .player import Player
from .strategy import Strategy


class Game:

    def __init__(self, board, players):
        self.board = board
        self.players = players

    def play(self):
        print("Let's play Monopoly!")


if __name__ == '__main__':
    board = Board('boards/uk_london')
    players = [Player(Strategy()) for i in range(4)]
    game = Game(board, players)
    game.play()

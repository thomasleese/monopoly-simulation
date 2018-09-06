from .board import Board
from .player import Player
from .strategy import Strategy


class Game:

    def __init__(self, board, players):
        self.board = board
        self.players = players

    def play(self):
        print("Let's play Monopoly!")

        while True:
            for player in self.players:
                player(self.board)


if __name__ == '__main__':
    board = Board('boards/uk_london')
    players = [Player(board.starting_money, Strategy()) for i in range(4)]
    game = Game(board, players)
    game.play()

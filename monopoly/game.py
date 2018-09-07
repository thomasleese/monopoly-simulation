from .board import Board
from .player import Player
from .strategy import Strategy


class Game:

    def __init__(self, board, players):
        self.board = board
        self.players = players

        for player in self.players:
            player.attach_to_board(self.board)

    def play(self):
        print("Let's play Monopoly!")

        while True:
            for player in self.players:
                player.play()


if __name__ == '__main__':
    board = Board('boards/uk_london')
    players = [Player(Strategy()) for i in range(4)]
    game = Game(board, players)
    game.play()

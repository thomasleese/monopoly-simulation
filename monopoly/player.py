class Player:

    def __init__(self, strategy):
        self.strategy = strategy
        self.money = 0
        self.position = 0
        self.properties = []
        self.cards = []
        self.in_jail = False

    def attach_to_board(self, board):
        self.board = board
        self.money = board.starting_money

    def play(self):
        dice, is_double = self.board.roll_dice()
        self.play_go(dice)

        if is_double:
            dice, is_double = self.board.roll_dice()
            self.play_go(dice)

            if is_double:
                _, is_double = self.board.roll_dice()
                self.go_to_jail()

    def go_to_jail(self):
        self.in_jail = True
        raise ValueError('I go to jail')

    def play_go(self, dice):
        print('I rolled a', dice)

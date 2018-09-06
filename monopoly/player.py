class Player:

    def __init__(self, money, strategy):
        self.money = money
        self.strategy = strategy
        self.position = 0
        self.properties = []
        self.cards = []
        self.in_jail = False

    def __call__(self, board):
        dice, is_double = board.roll_dice()
        self.play_go(dice)

        if is_double:
            dice, is_double = board.roll_dice()
            self.play_go(dice)

            if is_double:
                _, is_double = board.roll_dice()
                self.go_to_jail(board)

    def go_to_jail(self, board):
        self.in_jail = True
        raise ValueError('I go to jail')

    def play_go(self, dice):
        print('I rolled a', dice)

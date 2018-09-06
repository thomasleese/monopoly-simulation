class Player:

    def __init__(self, money, strategy):
        self.money = money
        self.strategy = strategy
        self.position = 0
        self.properties = []
        self.cards = []

    def __call__(self, board):
        raise ValueError("Help!")

import itertools

from .properties import Street


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
        self.think()

        dice, is_double = self.board.roll_dice()
        self.advance(dice)

        if is_double:
            dice, is_double = self.board.roll_dice()
            self.advance(dice)

            if is_double:
                _, is_double = self.board.roll_dice()
                self.go_to_jail()

    def go_to_jail(self):
        self.in_jail = True
        self.position = self.board.spaces.position('jail')

    def advance(self, spaces):
        self.advance_to(self.position + spaces)

    def advance_to(self, position):
        self.position = position
        if self.position >= len(self.board.spaces):
            self.position -= len(self.board.spaces)
            self.money += 200

        self.landed()

    def go_back(self, spaces):
        self.go_back_to(self.position - spaces)

    def go_back_to(self, position):
        self.position = position
        if self.position < 0:
            self.position += len(self.board.spaces)

        self.landed()

    def landed(self):
        space = self.board.spaces[self.position]
        print('Landed on:', space)
        space.play(self)

    def spend(self, money):
        if money > self.money:
            deficit = money - self.money
            self.strategy.make_money(self, deficit)

        if money > self.money:
            raise RuntimeError("Can't spend!")

        self.money -= money

    @property
    def houses(self):
        return sum(p.houses for p in self.properties if isinstance(p, Street))

    @property
    def hotels(self):
        return sum(p.hotels for p in self.properties if isinstance(p, Street))

    def think(self):
        self.strategy.think(self)

    @property
    def property_groups(self):
        groups = []

        for group, properties in itertools.groupby(self.properties, lambda p: p.group):
            properties = list(properties)
            if len(properties) == len(group.properties):
                groups.append(group)

        return groups

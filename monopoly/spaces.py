class Space:

    def __call__(self, player):
        raise NotImplementedError(
            'Must implement what happens when the player lands on this space.'
        )

    def attach_to_board(self, board):
        pass


class Go(Space):

    def __call__(self, player):
        player.money += 200


class Tax(Space):

    def __init__(self, amount):
        self.amount = amount

    def __call__(self, player):
        player.money -= self.amount


class Property(Space):

    def __init__(self, property_name, price):
        self.property_name = property_name
        self.price = price

    def attach_to_board(self, board):
        self.property = board.properties[self.property_name]


class Card(Space):

    def __init__(self, deck_name):
        self.deck_name = deck_name

    def attach_to_board(self, board):
        self.deck = board.cards[self.deck_name]


class Jail(Space):
    pass


class FreeParking(Space):
    pass


class GoToJail(Space):
    pass

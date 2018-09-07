class Space:

    def attach_to_board(self, board):
        pass

    def play(self, player):
        raise NotImplementedError(
            'Must implement what happens when the player lands on this space.'
        )


class Go(Space):

    def play(self, player):
        player.money += 200


class Tax(Space):

    def __init__(self, amount):
        self.amount = amount

    def play(self, player):
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

    def play(self, player):
        player.go_to_jail()

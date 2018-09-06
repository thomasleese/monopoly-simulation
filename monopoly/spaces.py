class Space:

    def __call__(self, player):
        raise NotImplementedError(
            'Must implement what happens when the player lands on this space.'
        )


class Go(Space):

    def __call__(self, player):
        player.money += 200


class Tax(Space):

    def __init__(self, amount):
        self.amount = amount

    def __call__(self, player):
        player.money -= self.amount


class Property(Space):

    def __init__(self, property, price):
        self.property = property
        self.price = price


class Card(Space):

    def __init__(self, deck):
        self.deck = deck


class Jail(Space):
    pass


class FreeParking(Space):
    pass


class GoToJail(Space):
    pass

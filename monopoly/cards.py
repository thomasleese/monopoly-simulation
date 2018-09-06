class Card:
    pass


class Advance(Card):

    def __init__(self, target):
        self.target = target


class GoBack(Card):

    def __init__(self, target):
        self.target = target


class GoToJail(Card):
    pass


class Pay(Card):

    def __init__(self, amount, pickup=None):
        self.amount = amount
        self.pickup = pickup


class Receive(Card):

    def __init__(self, amount, payer='bank'):
        if payer not in ['bank', 'players']:
            raise ValueError('Payer must either be bank or players.')

        self.amount = amount
        self.payer = payer


class GetOutOfJailFree(Card):
    pass


class StreetRepairs(Card):

    def __init__(self, house, hotel):
        self.house_cost = house
        self.hotel_cost = hotel

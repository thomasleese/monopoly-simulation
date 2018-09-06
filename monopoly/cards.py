class Card:

    def __call__(self, player):
        raise NotImplementedError(
            'Must implement what happens when the player lands on this card.'
        )

    def attach_to_board(self, board):
        pass


class Advance(Card):

    def __init__(self, target):
        self.target = target


class GoBack(Card):

    def __init__(self, target):
        self.target = target


class GoToJail(Card):

    def __call__(self, player):
        player.go_to_jail()


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

    def __call__(self, player):
        # TODO check the player has this card
        player.in_jail = False
        # TODO move this card back to the deck


class StreetRepairs(Card):

    def __init__(self, house, hotel):
        self.house_cost = house
        self.hotel_cost = hotel

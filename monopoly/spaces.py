class Space:

    def attach_to_board(self, board):
        pass

    def play(self, player):
        raise NotImplementedError(
            'Must implement what happens when the player lands on this space.'
        )


class Go(Space):

    name = 'go'

    def play(self, player):
        player.money += 200


class Tax(Space):

    def __init__(self, amount):
        self.amount = amount
        self.name = f'tax_{amount}'

    def play(self, player):
        player.money -= self.amount


class Property(Space):

    def __init__(self, property_name, price):
        self.name = property_name
        self.price = price

    def __str__(self):
        return f'Property({self.name})'

    def attach_to_board(self, board):
        self.property = board.properties[self.name]

    def play(self, player):
        if self.property.player is None:
            player.spend(self.price)
            self.property.bought(player)
        else:
            player.spend(self.property.rent)
            self.property.player.money += self.property.rent


class Card(Space):

    def __init__(self, deck_name):
        self.name = deck_name

    def attach_to_board(self, board):
        self.deck = board.cards[self.name]

    def play(self, player):
        self.deck.play(player)


class Jail(Space):

    name = 'jail'

    def play(self, player):
        pass


class FreeParking(Space):

    name = 'free_parking'

    def play(self, player):
        pass


class GoToJail(Space):

    name = 'go_to_jail'

    def play(self, player):
        player.go_to_jail()

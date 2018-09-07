class Deck:

    def __init__(self, cards):
        self.cards = cards

    def attach_to_board(self, board):
        for card in self.cards:
            card.deck = self
            card.attach_to_board(board)

    def take(self):
        return self.cards.pop()

    def insert(self, card):
        self.cards.insert(0, card)

    def play(self, player):
        card = self.take()
        print('Playing:', card)
        if card.play(player) is not False:
            self.insert(card)


class Card:

    deck = None

    def attach_to_board(self, board):
        pass

    def play(self, player):
        raise NotImplementedError(
            'Must implement what happens when the player plays this card.'
        )


class Advance(Card):

    def __init__(self, target):
        self.target = target

    def attach_to_board(self, board):
        self.target = board.spaces.position(self.target)

    def play(self, player):
        player.advance_to(self.target)


class GoBack(Card):

    def __init__(self, target):
        self.target = target
        self.absolute = None

    def attach_to_board(self, board):
        if isinstance(self.target, str):
            self.target = board.spaces.position(self.target)
            self.absolute = True
        else:
            self.absolute = False

    def play(self, player):
        if self.absolute:
            player.go_back_to(self.target)
        else:
            player.go_back(self.target)


class GoToJail(Card):

    def play(self, player):
        player.go_to_jail()


class Pay(Card):

    def __init__(self, amount, pickup=None):
        self.amount = amount
        self.pickup = pickup

    def attach_to_board(self, board):
        self.all_cards = board.cards

    def play(self, player):
        if self.pickup is None:
            player.spend(self.amount)
        else:
            strategy = player.strategy.pay_or_pickup(player, self)
            if strategy == 'pay':
                player.spend(self.amount)
            elif strategy == 'pickup':
                deck = self.all_cards[self.pickup]
                deck.play(player)


class Receive(Card):

    def __init__(self, amount, payer='bank'):
        if payer not in ['bank', 'players']:
            raise ValueError('Payer must either be bank or players.')

        self.amount = amount
        self.payer = payer

    def attach_to_board(self, board):
        self.all_players = set(board.players)

    def play(self, player):
        if self.payer == 'bank':
            player.money += self.amount
        elif self.payer == 'players':
            other_players = self.all_players - set([player])
            for other_player in other_players:
                other_player.spend(self.amount)
                player.money += self.amount


class GetOutOfJailFree(Card):

    player = None

    def play(self, player):
        if self.player is None:
            player.cards.append(self)
            self.player = player
            return False

        if not self in player.cards:
            raise ValueError("Player doesn't have this card!")

        player.in_jail = False
        player.cards.remove(self)

        self.deck.insert(card)


class StreetRepairs(Card):

    def __init__(self, house, hotel):
        self.house_cost = house
        self.hotel_cost = hotel

    def calculate_total(self, player):
        houses = self.house_cost * player.houses
        hotels = self.hotel_cost * player.hotels
        return houses + hotels

    def play(self, player):
        player.spend(self.calculate_total(player))

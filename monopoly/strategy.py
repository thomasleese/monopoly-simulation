class Strategy:

    def think(self, player):
        raise NotImplementedError()

    def pay_or_pickup(self, player, card):
        raise NotImplementedError()

    def make_money(self, player, amount):
        raise NotImplementedError()


class BasicStrategy(Strategy):

    def think(self, player):
        print(player.properties)
        for group in player.property_groups:
            raise RuntimeError('I could buy!')

    def pay_or_pickup(self, player, card):
        if player.money > card.amount:
            return 'pay'
        else:
            return 'pickup'

    def make_money(self, player, amount):
        print('Trying to make', amount, 'for', player)

        # deal cards
        # sell hotels
        # sell houses

        # mortage property
        for property in player.properties:
            if property.can_be_mortgaged:
                print('Mortgage:', property)

        # sell property

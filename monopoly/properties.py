class Group:

    def __init__(self, name):
        self.name = name
        self.properties = []

    def attach_to_board(self, board):
        pass


class Property:

    def __init__(self, name, mortgage_value, rents):
        self.name = name
        self.mortgage_value = mortgage_value
        self.rents = rents
        self._group = None
        self.player = None
        self.mortgaged = False

    def attach_to_board(self, board):
        pass

    @property
    def group(self):
        return self._group

    def add_to_group(self, group):
        assert self.group is None
        self._group = group
        group.properties.append(self)

    @property
    def rent(self):
        return self.rents[0]

    def bought(self, player):
        if self.player is not None:
            raise RuntimeError('Already bought!')

        player.properties.append(self)
        self.player = player

    @property
    def can_be_mortgaged(self):
        return not self.mortgaged


class Street(Property):

    def __init__(self, name, mortgage_value, rent, house_price):
        super().__init__(name, mortgage_value, rent)
        self.house_price = house_price
        self.houses = 0
        self.hotels = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Street({self.name})'

    @property
    def can_be_mortgaged(self):
        return not self.mortgaged and self.houses == 0 and self.hotels == 0


class Station(Property):
    pass


class Utility(Property):
    pass

class Group:

    def __init__(self, name):
        self.name = name
        self.properties = []


class Property:

    def __init__(self, name, mortgage_value, rent):
        self.name = name
        self.mortgage_value = mortgage_value
        self.rent = rent
        self._group = None

    @property
    def group(self):
        return self._group

    def add_to_group(self, group):
        assert self.group is None
        self._group = group
        group.properties.append(self)


class Street(Property):

    def __init__(self, name, mortgage_value, rent, house_price):
        super().__init__(name, mortgage_value, rent)
        self.house_price = house_price


class Station(Property):
    pass


class Utility(Property):
    pass

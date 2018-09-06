from collections import UserDict, UserList
from pathlib import Path

import yaml

from . import cards, spaces
from .properties import Group, Property, Station, Street, Utility


class Properties(UserDict):

    def __init__(self, config):
        super().__init__()

        for group_name, properties in config.items():
            group = Group(group_name)
            self.add_properties(group, properties)

    def add_properties(self, group, config):
        if group.name == 'stations':
            self.add_station_or_utility(group, Station, config)
        elif group.name == 'utilities':
            self.add_station_or_utility(group, Utility, config)
        else:
            for name, street_config in config.items():
                self.add_street(group, name, street_config)

    def add_station_or_utility(self, group, cls, config):
        mortgage_value = config['mortgage']
        rent = config['rent']
        for name in config['names']:
            self.add_property(group, cls(name, mortgage_value, rent))

    def add_street(self, group, name, config):
        street = Street(
            name, config['mortgage'], config['rent'], config['house']
        )

        self.add_property(group, street)

    def add_property(self, group, property):
        property.add_to_group(group)
        self.data[property.name] = property


class Deck(UserList):

    card_types = {
        'advance': cards.Advance,
        'go_back': cards.GoBack,
        'go_to_jail': cards.GoToJail,
        'pay': cards.Pay,
        'receive': cards.Receive,
        'get_out_of_jail_free': cards.GetOutOfJailFree,
        'street_repairs': cards.StreetRepairs,
    }

    def __init__(self, config):
        super().__init__()

        for item in config:
            self.data.append(self.load_card(item))

    def load_card(self, config):
        for name, cls in self.card_types.items():
            if name in config:
                if isinstance(config, str):
                    return cls()
                else:
                    arg = config[name]
                    del config[name]

                    if isinstance(arg, dict):
                        args = []
                        kwargs = arg
                    else:
                        args = [arg]
                        kwargs = config

                    return cls(*args, **kwargs)

        raise ValueError(f'Unknown card: {config}')


class Cards(UserDict):

    def __init__(self, config):
        super().__init__()

        for name, cards in config.items():
            self.data[name] = Deck(cards)


class Spaces(UserList):

    def __init__(self, config):
        super().__init__()

        for item in config:
            self.data.append(self.load_space(item))

    def load_space(self, config):
        if config == 'go':
            return spaces.Go()
        elif config == 'jail':
            return spaces.Jail()
        elif config == 'free_parking':
            return spaces.FreeParking()
        elif config == 'go_to_jail':
            return spaces.GoToJail()
        elif 'tax' in config:
            return spaces.Tax(config['tax'])
        elif 'card' in config:
            return spaces.Card(config['card'])
        else:
            name, price = list(config.items())[0]
            return spaces.Property(name, price)

        raise ValueError(f'Unknown space: {config}')

class Board:

    def __init__(self, filename):
        self.path = Path(filename)

        self.load_rules()
        self.load_properties()
        self.load_cards()
        self.load_spaces()

    def load_config(self, part):
        with (self.path / f'{part}.yaml').open('r') as file:
            return yaml.safe_load(file)

    def load_rules(self):
        config = self.load_config('rules')

        self.houses = config['houses']
        self.hotels = config['hotels']

    def load_properties(self):
        config = self.load_config('properties')
        self.properties = Properties(config)

    def load_cards(self):
        config = self.load_config('cards')
        self.cards = Cards(config)

    def load_spaces(self):
        config = self.load_config('spaces')
        self.spaces = Spaces(config)

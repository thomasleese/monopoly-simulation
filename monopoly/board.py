from collections import UserDict
from pathlib import Path

import yaml

from . import spaces
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

    def load_spaces(self):
        config = self.load_config('spaces')

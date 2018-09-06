from pathlib import Path

import yaml

from . import spaces


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

    def load_properties(self):
        config = self.load_config('properties')

    def load_cards(self):
        config = self.load_config('cards')

    def load_spaces(self):
        config = self.load_config('spaces')

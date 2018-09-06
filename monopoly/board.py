from . import spaces


class Board:

    def __init__(self):
        self.spaces = [
            spaces.Go(),
        ]

    @classmethod
    def from_config(cls, filename):
        return cls()

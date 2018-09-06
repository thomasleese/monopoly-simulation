class Space:

    def __call__(self, player):
        raise NotImplementedError(
            'Must implement what happens when the player lands on this space.'
        )


class GoSpace(Space):

    def __call__(self, player):
        player.money += 200


class Board:

    def __init__(self):
        self.spaces = [
            GoSpace(),
        ]

from unittest.mock import Mock

from monopoly.spaces import Go


def test_go():
    player = Mock(money=0)
    Go().play(player)
    assert player.money == 200

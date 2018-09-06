from unittest.mock import Mock

from monopoly.board import GoSpace


def test_go_space():
    player = Mock(money=0)
    GoSpace()(player)
    assert player.money == 200

from monopoly import Board


def test_loads_uk_london():
    board = Board('boards/uk_london')

    assert board.houses == 32
    assert board.hotels == 12

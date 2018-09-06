from monopoly import Board


def test_loads_uk_london():
    assert Board.from_config('uk_london')

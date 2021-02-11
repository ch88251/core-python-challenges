import pytest
from src.main.problems.birthday_cake_candles import birthday_cake_candles


testdata = [
    ([1,2,3,4,5], 1),
    ([2,4,6,8,3], 1),
    ([0,0,0,0,0], 5),
    ([2,4,1,4,7], 1),
    ([2,2,2,9,9], 2),
    ([2,2,2,2,9], 1),
    ([5,5,9,9,9], 3),
]


@pytest.mark.parametrize("input,expected", testdata)
def test_scenario1(input, expected):
    count = birthday_cake_candles(input)
    assert count == expected

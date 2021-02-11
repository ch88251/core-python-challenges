import pytest
from src.main.problems.mini_max_sum import mini_max_sum


testdata = [
    ([1,2,3,4,5], "10 14"),
    ([2,4,6,8,3], "15 21"),
    ([0,0,0,0,0], "0 0"),
]


@pytest.mark.parametrize("input,expected", testdata)
def test_scenario1(input, expected, capsys):
    mini_max_sum(input)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'

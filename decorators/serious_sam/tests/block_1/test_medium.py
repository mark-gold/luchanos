import pytest

from block_1.medium import custom_sum, custom_sum_modified


def test_custom_sum():
    assert custom_sum(0) == 0
    assert custom_sum(1, 2) == 3
    assert custom_sum(1, 2, 3) == 6
    assert custom_sum() is None
    assert custom_sum('') == ''
    assert custom_sum([]) == []
    assert custom_sum({}) == {}
    assert custom_sum('hello', ',', ' ', 'world', '!') == 'hello, world!'


def test_custom_sum_modified():
    assert custom_sum_modified(1, 2, 3, 4) == 10
    assert custom_sum_modified(1, -1, 2, -2, 42) == 42
    assert custom_sum_modified(0, 0, 0, 0, 1, 2, 3, 4) == 10
    assert custom_sum_modified(1, 2, 3, 4, e=1, f=-1, g=0) == 10

    with pytest.raises(Exception) as exc_info:
        custom_sum_modified(1)
    assert exc_info.typename == 'TypeError'
    assert str(exc_info.value) == "custom_sum_modified() missing 3 required positional arguments: 'b', 'c', and 'd'"

    with pytest.raises(Exception) as exc_info:
        custom_sum_modified(1, 2, 3, 4, a=2)
    assert exc_info.typename == 'TypeError'
    assert str(exc_info.value) == "custom_sum_modified() got multiple values for argument 'a'"



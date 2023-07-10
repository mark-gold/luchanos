import pytest

from block_1.easy import multiply_and_modify


def test_multiply_and_modify_positive():
    assert multiply_and_modify('luchanos', 1) == 'luchanos'
    assert multiply_and_modify('luchanos', 2) == 'luchanosLUCHANOS'
    assert multiply_and_modify('luchanos', 3) == 'luchanosLUCHANOSluchanos'
    assert multiply_and_modify('luchanos', 4) == 'luchanosLUCHANOSluchanosLUCHANOS'


def test_multiply_and_modify_negative():
    with pytest.raises(Exception) as exc_info:
        multiply_and_modify('luchanos', 'incorrect_multiplier_type')
    assert str(exc_info.value) == 'Incorrect type of multiplier, it must be positive integer object.'

    with pytest.raises(Exception) as exc_info:
        multiply_and_modify('luchanos', 0)
    assert str(exc_info.value) == 'Incorrect value of multiplier, it must be positive integer object.'

    with pytest.raises(Exception) as exc_info:
        multiply_and_modify(True, 0)
    assert str(exc_info.value) == 'Incorrect type of input string, it must be string object.'

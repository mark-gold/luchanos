from block_1.hard import custom_sum_hard


def test_custom_sum_hard():
    assert custom_sum_hard(1, 2, 3, 4) == 10
    assert custom_sum_hard(1, 2, 3, 4, 5) == 15
    assert custom_sum_hard(1, 2, 3, 4, 5, 6) == 21
    assert custom_sum_hard(1, 2, 3, 4, kwarg=-1) == 9
    assert custom_sum_hard(1, 2, 3, 4, 5, 6, 7, kwarg_1=-1, kwarg_2=-1, kwarg_3=-1) == 20

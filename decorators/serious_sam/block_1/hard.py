"""
Модифицировать функцию таким образом, чтобы для суммирования брались только обязательные аргументы, первые
2 аргумента из дополнительных позиционных аргументов и любой аргумент из дополнительных аргументов (если они есть),
переданных по ключу (если они есть)
"""


def custom_sum_hard(a, b, c, d, *args, **kwargs):
    result = a + b + c + d
    if args:
        for index, arg in enumerate(args):
            if index < 2:
                result += arg
            else:
                break
    if kwargs:
        for kwarg in kwargs:
            result += kwargs[kwarg]
            break
    return result

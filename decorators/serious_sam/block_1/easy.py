"""
1. Написать простую функцию, которая на вход принимает строку ('test') и целое число (3),
а возвращает строку вида 'testTESTtest' - исходную строку, умноженную на 3, в разном регистре.
2. Записать эту функцию в произвольную переменную. Напечатать эту переменную на экран. Что вы видите?
3. Вызвать функцию суммирования через переменную, в которую вы только что её записали.
"""


# 1. Написать простую функцию, которая на вход принимает строку ('test') и целое число (3),
# а возвращает строку вида 'testTESTtest' - исходную строку, умноженную на 3, в разном регистре.
def multiply_and_modify(input_string: str, multiplier: int) -> str:
    """

    :param input_string: random string, let it be 'test'
    :param multiplier: positive integer number, let it be 4
    :return: string, in our case 'testTESTtestTEST'
    """
    if isinstance(input_string, str) is False:
        raise ValueError('Incorrect type of input string, it must be string object.')
    if isinstance(multiplier, int) is False:
        raise ValueError('Incorrect type of multiplier, it must be positive integer object.')
    if multiplier <= 0:
        raise ValueError('Incorrect value of multiplier, it must be positive integer object.')
    list_with_values = [input_string if i % 2 == 0 else input_string.upper() for i in range(multiplier)]
    return ''.join(list_with_values)


# 2. Записать эту функцию в произвольную переменную. Напечатать эту переменную на экран. Что вы видите?
"""
Вижу следующее:
var = multiply_and_modify
print(var): <function multiply_and_modify at 0x1032f3d90>
"""

# 3. Вызвать функцию суммирования через переменную, в которую вы только что её записали.
"""
Если я правильно понял задание, то я должен вызывать функцию через новую переменную-ссылку, то есть var('test', 3)
Результат будет таким же как и для вызова multiply_and_modify('test', 3) --> testTESTtest. 
Причина: функция одна и та же, просто ссылаться на неё можно через разные переменные.
"""

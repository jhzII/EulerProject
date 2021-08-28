# Перестановка - это упорядоченная выборка объектов.
# К примеру, 3124 является одной из возможных перестановок из цифр 1, 2, 3 и 4.
# Если все перестановки приведены в порядке возрастания или алфавитном порядке,
# то такой порядок будем называть словарным.
# Словарные перестановки из цифр 0, 1 и 2 представлены ниже:
# 012   021   102   120   201   210
# Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?
import math
from typing import List


def f(digits: List[str],  result: List[str], start: str = ''):
    if len(digits) == 1:
        result.append(start + digits[0])
    else:
        for i in range(0, len(digits)):
            f(digits[0:i]+digits[i+1:], result, start + digits[i])


def g(digits: List[str], index, start: str = ''):
    length = len(digits)
    if length == 1:
        return start + digits[0]

    quantity = math.factorial(length-1)
    next_digit = index // quantity
    index = index % quantity

    return g(digits[0:next_digit]+digits[next_digit+1:], index, start + digits[next_digit])


if __name__ == '__main__':
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # arr = []
    # f(DIGITS, arr)
    # print(arr[999999])

    print(g(DIGITS, 1000000-1))
    # 2783915460

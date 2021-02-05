# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

from functools import reduce


def min_common_divisible(end):
    """ Результатом является самое маленькое число, которое делится без остатка на все числа от 1 до end.

        end > 1
    """

    multipliers = []

    for i in range(2, end+1):
        number = i
        for multiplier in multipliers:
            if number % multiplier == 0:
                number /= multiplier

        if number > 1:
            multipliers.append(number)

    return reduce(lambda r, m: r * m, multipliers)


if __name__ == '__main__':
    print(min_common_divisible(20))

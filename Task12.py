# Последовательность треугольных чисел образуется путем сложения натуральных чисел.
# К примеру, 7-е треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Перечислим делители первых семи треугольных чисел:
#
#  1: 1
#  3: 1, 3
#  6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28
# Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.
#
# Каково первое треугольное число, у которого более пятисот делителей?


def get_number_of_divisors(value: int):
    """ Возвращает количество делителей. """

    number_of_divisors = 0

    for i in range(1, value + 1):
        quotient = value / i

        if quotient < i:
            return number_of_divisors * 2
        if quotient == i:
            return number_of_divisors * 2 + 1

        if quotient % 1 == 0:
            number_of_divisors += 1

    return 1  # сработает только для 1


def min_triangle_value_with_n_divider(n: int = 500) -> int:
    triangle_value = 1
    number_triangle_value = 1
    number_of_divisors = 1

    while number_of_divisors <= n:
        number_triangle_value += 1
        triangle_value += number_triangle_value

        number_of_divisors = get_number_of_divisors(triangle_value)

    return triangle_value


if __name__ == '__main__':
    print(min_triangle_value_with_n_divider(500))

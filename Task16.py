# 2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
# Какова сумма цифр числа 2^1000?


def sum_of_digits(value: int) -> int:
    result = 0
    while value > 0:
        result += value % 10
        value //= 10

    return result


if __name__ == '__main__':
    print(sum_of_digits(2 ** 1000))

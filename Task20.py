# n! означает n × (n − 1) × ... × 3 × 2 × 1
# Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Найдите сумму цифр в числе 100!.
import math


def factorial_rec(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)


def factorial(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n -= 1

    return result


def sum_of_digits(n: int) -> int:
    result = 0

    while n > 0:
        result += n % 10
        n //= 10

    return result


if __name__ == '__main__':
    print(sum_of_digits(math.factorial(100)))
    # 648

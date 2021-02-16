# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
# Найдите сумму всех простых чисел меньше двух миллионов.
from functools import reduce


def sum_simple_numbers(limit: int) -> int:
    prime_numbers = [2]
    number = 2

    while number < limit:
        for i in prime_numbers:
            if number % i == 0:
                break
            if number / i < i:
                prime_numbers.append(number)
                break
        number += 1

    return reduce(lambda s, n: s + n, prime_numbers)


if __name__ == '__main__':
    print(sum_simple_numbers(2000000))

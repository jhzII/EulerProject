# Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
# Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой,
#   а каждое из чисел a и b - дружественным числом.
# Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110,
#   поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.
# Подсчитайте сумму всех дружественных чисел меньше 10000.
import math


def d(n):
    # n > 1
    amount = 1
    limit = math.sqrt(n)

    if limit % 1 == 0:
        amount += limit
    else:
        limit += 1

    for i in range(2, int(limit)):
        quotient = n / i
        if quotient % 1 == 0:
            amount += i
            amount += quotient

    return amount


def sum_of_friendly_numbers(n):
    dict_of_d = {}
    set_of_fn = set()

    for i in range(2, n):
        dict_of_d[i] = d(i)

    for key, value in dict_of_d.items():
        if key != value and value in dict_of_d and dict_of_d[value] == key:
            set_of_fn.add(key)
            set_of_fn.add(value)

    return sum(set_of_fn)


if __name__ == '__main__':
    print(sum_of_friendly_numbers(10000))
    # 31626

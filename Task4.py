# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел
import math


def is_palindrome(number):
    str_number = str(number)
    for i in range(len(str_number)//2):
        if str_number[i] != str_number[len(str_number) - 1 - i]:
            return False
    return True


def max_palindrome(n, *, include_index=False):
    """ Ищет максимальный палиндром при умножении чисел n разрядности.

        include_index - включает в результат множители палиндрома.
    """

    max_p = -1
    max_p_i = max_p_j = -1

    n = int(math.pow(10, n))
    i = j = n - 1

    while i >= n // 10 and i * j > max_p:
        while j >= n // 10:
            number = j * i
            if is_palindrome(number) and number > max_p:
                max_p = number
                max_p_i = i
                max_p_j = j
            j -= 1
        i -= 1
        j = i

    return (max_p, max_p_i, max_p_j) if include_index else max_p


if __name__ == '__main__':
    print(max_palindrome(3, include_index=True))

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел
import math


def is_palindrome(number):
    str_number = str(number)
    for i in range(len(str_number)//2):
        if str_number[i] != str_number[len(str_number) - 1 - i]:
            return False
    return True


def max_palindrome(n):
    """ Ищет максимальный палиндром при умножении чисел n разрядности.

        Обход по матрице в обратном порядке,
        вызов break, если нет шансов найти больше.
    """

    n = int(math.pow(10, n))
    max_p = -1
    i = j = n - 1

    while i >= n // 10 and i * j > max_p:
        while j >= n // 10:
            number = j * i
            if is_palindrome(number) and number > max_p:
                max_p = number
            j -= 1
            if i * j < max_p:
                break
        j = n - 1
        i -= 1
        if i * j < max_p:
            break
    return max_p


print(max_palindrome(5))

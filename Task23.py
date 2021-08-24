# Совершенным числом называется число, у которого сумма его делителей равна самому числу. Например,
# сумма делителей числа 28 равна 1 + 2 + 4 + 7 + 14 = 28, что означает, что число 28 является совершенным числом.
# Число n называется недостаточным, если сумма его делителей меньше n,
# и называется избыточным, если сумма его делителей больше n.
# Так как число 12 является наименьшим избыточным числом (1 + 2 + 3 + 4 + 6 = 16), наименьшее число,
# которое может быть записано как сумма двух избыточных чисел, равно 24.
# Используя математический анализ, можно показать, что все целые числа больше 28123 могут быть записаны как сумма двух
# избыточных чисел. Эта граница не может быть уменьшена дальнейшим анализом, даже несмотря на то, что наибольшее число,
# которое не может быть записано как сумма двух избыточных чисел, меньше этой границы.
#
# Найдите сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных чисел.

# . . . #

# список избыточных чисел
# список не возможных двух избыточных
# сумма
from Task21 import d as get_sum_of_divisors

TOTAL = 28123


def get_list_excesses_numbers():
    list_excesses_numbers = []

    for i in range(2, TOTAL + 1):
        if i < get_sum_of_divisors(i):
            list_excesses_numbers.append(i)

    return list_excesses_numbers


def get_list_excesses_numbers_not_sum_of_two(list_excesses_numbers):
    list_excesses_numbers_sum_of_two = set()
    limit = len(list_excesses_numbers)

    for i in range(0, limit):
        for j in range(i, limit):
            amount = list_excesses_numbers[i] + list_excesses_numbers[j]
            if amount > TOTAL:
                break
            list_excesses_numbers_sum_of_two.add(amount)

    return [i for i in range(1, TOTAL) if i not in list_excesses_numbers_sum_of_two]


if __name__ == '__main__':
    print(sum(get_list_excesses_numbers_not_sum_of_two(get_list_excesses_numbers())))
    # 4179871

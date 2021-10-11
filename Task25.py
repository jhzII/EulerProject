# Последовательность Фибоначчи определяется рекурсивным правилом:
# Fn = Fn−1 + Fn−2, где F1 = 1 и F2 = 1.
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F12 = 89
# F12 = 144
# Двенадцатый член F12 - первый член последовательности, который содержит три цифры.
#
# Каков порядковый номер первого члена последовательности Фибоначчи, содержащего 1000 цифр?


def get_ordinal_number_of_first_fib_number_with_n_digits(n: int) -> int:
    ordinal = 1
    previous_value = 0
    value = 1

    while len(str(value)) < n:
        previous_value, value = value, previous_value + value
        ordinal += 1

    return ordinal


if __name__ == '__main__':
    print(get_ordinal_number_of_first_fib_number_with_n_digits(1000))  # 4782

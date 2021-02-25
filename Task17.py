# Если записать числа от 1 до 5 английскими словами (one, two, three, four, five),
# то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
# Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
# Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв,
# число 115 (one hundred and fifteen) - из 20 букв.
# Использование "and" при записи чисел соответствует правилам британского английского.


numbers_lengths = {
    'and': 3,
    0: 0,
    1: 3,  # one
    2: 3,  # two
    3: 5,  # three
    4: 4,  # four
    5: 4,  # five
    6: 3,  # six
    7: 5,  # seven
    8: 5,  # eight
    9: 4,  # nine
    10: 3,  # ten
    11: 6,  # eleven
    12: 6,  # twelve
    13: 8,  # thirteen
    14: 8,  # fourteen
    15: 7,  # fifteen
    16: 7,  # sixteen
    17: 9,  # seventeen
    18: 8,  # eighteen
    19: 8,  # nineteen
    20: 6,  # twenty
    30: 6,  # thirty
    40: 5,  # forty
    50: 5,  # fifty
    60: 5,  # sixty
    70: 7,  # seventy
    80: 6,  # eighty
    90: 6,  # ninety
    100: 7,  # hundred
    1000: 8,  # thousand
}


def get_number_length(value: int) -> int:
    """ 0 < value < 10000 """

    number_length = 0

    two_last_digit = value % 100

    if two_last_digit < 21:
        number_length += numbers_lengths[two_last_digit]
        value //= 100
    else:
        for n in range(2):
            number_length += numbers_lengths[value % 10 * 10**n]
            value //= 10

    if value <= 0:
        return number_length

    if two_last_digit:
        number_length += numbers_lengths['and']

    for n in range(2, 4):
        digit = value % 10
        if digit:
            number_length += numbers_lengths[digit]
            number_length += numbers_lengths[10**n]
        value //= 10
        if value <= 0:
            return number_length

    return number_length


if __name__ == '__main__':
    total = 0

    for i in range(1, 1000+1):
        total += get_number_length(i)

    print(total)

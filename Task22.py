# Используйте names.txt, текстовый файл размером 46 КБ, содержащий более пяти тысяч имен.
# Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени
# и умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.
#
# Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53)
# является 938-м в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.
#
# Какова сумма очков имен в файле?
import json
from typing import List


def get_names():
    with open('./files/p022_names.txt') as f:
        data = f'[{f.read()}]'
        return json.loads(data)


def get_amount_of_points(nms: List[str]):
    names = nms[:]
    names.sort()

    amount_of_points = 0
    i = 1
    for name in names:
        amount_of_ch = 0
        for ch in name:
            amount_of_ch += ord(ch) - 64  # ORD('A') == 65
        amount_of_points += amount_of_ch * i
        i += 1

    return amount_of_points


if __name__ == '__main__':
    print(get_amount_of_points(get_names()))  # 871198282

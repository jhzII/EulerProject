# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
#    a^2 + b^2 = c^2
# Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.


def abc1000():
    for i in range(1, 333):
        a = i
        b = (1000000 - 2000*a)/(2000 - 2*a)

        if b % 1 != 0:
            continue

        c = 1000 - a - b

        if a**2 + b**2 == c**2:
            return a, b, c, a*b*c


if __name__ == '__main__':
    print(abc1000())

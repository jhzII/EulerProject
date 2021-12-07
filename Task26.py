# Единичная дробь имеет 1 в числителе. Десятичные представления единичных дробей со знаменателями от 2 до 10 даны ниже:
# 1/2	=	0.5
# 1/3	=	0.(3)
# 1/4	=	0.25
# 1/5	=	0.2
# 1/6	=	0.1(6)
# 1/7	=	0.(142857)
# 1/8	=	0.125
# 1/9	=	0.(1)
# 1/10	=	0.1
# Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры.
# Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.
#
# Найдите значение d < 1000,
# для которого 1/d в десятичном виде содержит самую длинную повторяющуюся последовательность цифр.


if __name__ == '__main__':
    d = None
    max_length = 0

    for i in range(1, 1000):
        current_rem = 10 % i
        remains = [current_rem]

        while current_rem % i != 0:
            current_rem = current_rem * 10 % i
            if current_rem in remains:
                length = len(remains) - remains.index(current_rem)
                if length > max_length:
                    max_length = length
                    d = i
                break

            remains.append(current_rem)

    print(d)

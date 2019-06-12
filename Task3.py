# Каков самый большой делитель числа 600851475143, являющийся простым числом?


def greatest_simple_divisor(number):
    dividers = []

    for i in range(2, int(number ** 0.5) + 1):
        if number % i != 0:
            continue

        for x in dividers:
            if i % x == 0:
                break
        else:
            dividers.append(i)

    return -1 if len(dividers) == 0 else dividers[len(dividers) - 1]


print(greatest_simple_divisor(600851475143))

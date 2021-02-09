# Какое число является 10001-м простым числом?


def prime_number(order):
    prime_numbers = [2]
    number = 2

    while len(prime_numbers) < order:
        for i in prime_numbers:
            if number % i == 0:
                break
            if number / i < i:
                prime_numbers.append(number)
                break
        number += 1

    return prime_numbers[-1]


if __name__ == '__main__':
    print(prime_number(10001))

# Найдите сумму всех четных элементов ряда Фибоначчи,
# которые не превышают четыре миллиона. (Последовательность начинается с 1 и 2)

low = 1
high = 2
amount = 0

while high < 4000000:
    if high % 2 == 0:
        amount += high
    low, high = high, low + high

print(amount)

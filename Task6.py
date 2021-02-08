# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
from functools import reduce


def difference_sum_of_sq_and_sq_of_sum(n):
    sq_of_sum = reduce(lambda r, i: r + i, range(1, n+1))**2

    sum_of_sq = reduce(lambda r, i: r + i**2, range(1, n+1))

    return sq_of_sum - sum_of_sq


if __name__ == '__main__':
    print(difference_sum_of_sq_and_sq_of_sum(100))

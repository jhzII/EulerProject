# Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
# существует ровно 6 маршрутов до правого нижнего угла сетки.
# Сколько существует таких маршрутов в сетке 20×20?


def get_number_of_routes(n: int) -> int:
    """ n > 0 """

    n += 1
    matrix = [[0 for i in range(n)] for i in range(n)]

    matrix[0][0] = 1
    for i in range(1, n):
        matrix[0][i] = 1
        matrix[i][0] = 1

    for i in range(1, n):
        for j in range(1, n):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[n-1][n-1]


if __name__ == '__main__':
    print(get_number_of_routes(20))

"""
В левом верхнем углу прямоугольной таблицы размером N×M находится черепашка.
В каждой клетке таблицы записано некоторое число. Черепашка может перемещаться вправо или вниз,
при этом маршрут черепашки заканчивается в правом нижнем углу таблицы.

Подсчитаем сумму чисел, записанных в клетках, через которую проползла черепашка
(включая начальную и конечную клетку).
Найдите наибольшее возможное значение этой суммы и маршрут, на котором достигается эта сумма.
"""


def main():
    n, m = map(int, input().split())
    a = [[int(x) for x in input().split()] for _ in range(n)]

    dp = [[0] * m for _ in range(n)]
    parent = [[""] * m for _ in range(n)]
    dp[0][0] = a[0][0]

    # Первая строка
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + a[0][j]
        parent[0][j] = "R"

    # Первый столбец
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + a[i][0]
        parent[i][0] = "D"

    # Остальные клетки
    for i in range(1, n):
        for j in range(1, m):
            if dp[i - 1][j] >= dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j] + a[i][j]
                parent[i][j] = "D"
            else:
                dp[i][j] = dp[i][j - 1] + a[i][j]
                parent[i][j] = "R"

    # Восстановление пути
    path = []
    i, j = n - 1, m - 1

    while i != 0 or j != 0:
        path.append(parent[i][j])
        if parent[i][j] == "D":
            i -= 1
        else:
            j -= 1

    path.reverse()

    # Отладочный вывод
    # print("-" * 20)
    # print(*dp, sep="\n")
    # print("-" * 20)
    # print(*parent, sep="\n")
    # print("-" * 20)

    print(dp[n - 1][m - 1])
    print(*path)


if __name__ == "__main__":
    main()

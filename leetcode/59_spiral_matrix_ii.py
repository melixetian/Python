#!/usr/bin/env python3

"""
Выведите таблицу размером nxn,
заполненную числами от 1 до n^2 по спирали,
выходящей из левого верхнего угла и
закрученной по часовой стрелке, как показано в примере
"""

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
cnt = 1
ix, jx, ic, jc = 0, 0, 0, 0

for k in range(n * m):
    if cnt == n * m + 1:
        break
    dr = k % 4
    if dr == 0:
        for j in range(jx, m - jx):
            matrix[ic][j] = cnt
            cnt += 1
        jc = j
        ix += 1
    elif dr == 1:
        for i in range(ix, n - ix + 1):
            matrix[i][jc] = cnt
            cnt += 1
        ic = i
        jx += 1
    elif dr == 2:
        for j in range(jc - 1, jx - 2, -1):
            matrix[ic][j] = cnt
            cnt += 1
        jc = j
    elif dr == 3:
        for i in range(ic - 1, ix - 1, -1):
            matrix[i][jc] = cnt
            cnt += 1
        ic = i

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()

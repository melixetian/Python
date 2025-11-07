#!/usr/bin/env python3

"""
Сложение матриц
"""

n, m = [int(i) for i in input().split()]
matrA = [[None] * m] * n
matrB = [[None] * m] * n

for i in range(n):
    matrA[i] = [int(j) for j in input().split()]

for i in range(n):
    matrB[i] = [int(j) for j in input().split()]

matrC = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrC[i][j] = matrA[i][j] + matrB[i][j]

for row in matrC:
    print(*row)

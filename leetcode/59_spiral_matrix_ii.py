"""
LC 59. Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/

Вернуть матрицу n×n, заполненную числами от 1 до n² по спирали
по часовой стрелке, начиная с левого верхнего угла.
"""


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        value = 1

        for start in range(n // 2):
            end = n - 1 - start
            for col in range(start, end):
                matrix[start][col] = value
                value += 1
            for row in range(start, end):
                matrix[row][end] = value
                value += 1
            for col in range(end, start, -1):
                matrix[end][col] = value
                value += 1
            for row in range(end, start, -1):
                matrix[row][start] = value
                value += 1

        if n % 2:
            center = n // 2
            matrix[center][center] = value

        return matrix

"""
LC 6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        matr = [[] for _ in range(numRows)]
        row, dir = 0, 1

        for ch in s:
            matr[row].append(ch)
            if row == 0:
                dir = 1
            elif row == numRows - 1:
                dir = -1
            row += dir

        return "".join("".join(row) for row in matr)

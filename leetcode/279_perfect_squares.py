"""
LC 279. Perfect Squares
https://leetcode.com/problems/perfect-squares/

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of
some integer with itself.

For example, 1, 4, 9 and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9
"""


from math import isqrt


class Solution:
    def numSquares(self, n: int) -> int:
        # Каждую сумму можно набрать единицами.
        counts = list(range(n + 1))
        for root in range(2, isqrt(n) + 1):
            square = root * root
            for total in range(square, n + 1):
                counts[total] = min(counts[total], counts[total - square] + 1)
        return counts[n]

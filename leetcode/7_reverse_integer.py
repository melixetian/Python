"""
LC 7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1

        sign = -1 if x < 0 else 1
        x *= sign

        result = 0
        while x:
            digit = x % 10
            x //= 10

            if result > (MAX_INT - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result

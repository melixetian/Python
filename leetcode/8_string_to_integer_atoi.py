"""
LC 8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -(2**31)

        s = s.strip()
        if not s:
            return 0

        sign = -1 if s[0] == "-" else 1
        if s[0] in "+-":
            s = s[1:]

        result = 0
        for ch in s:
            if ch.isdigit():
                result = result * 10 + int(ch)
            else:
                break

        result *= sign
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result

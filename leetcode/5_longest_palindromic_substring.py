"""
LC 5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s

        start, end = 0, 0

        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(n):
            # нечётный центр
            l1, r1 = expand(i, i)
            # чётный центр
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]

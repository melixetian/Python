"""
LC 28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        i = 0
        while i < n and n - i >= m:
            if n - i < m:
                break

            if haystack[i] == needle[0]:
                j = 0
                ans = i
                while j < m and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                if j == m:
                    return ans
                else:
                    i = ans

            i += 1

        return -1

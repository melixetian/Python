"""
LC 14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first = strs[0]
        for index, char in enumerate(first):
            for word in strs:
                if index == len(word) or word[index] != char:
                    return first[:index]

        return first

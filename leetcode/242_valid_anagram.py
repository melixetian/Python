"""
LC 242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ch_map = dict()
        for i in range(len(s)):
            ch_map[s[i]] = ch_map.get(s[i], 0) + 1
            ch_map[t[i]] = ch_map.get(t[i], 0) - 1

        for num in ch_map.values():
            if num != 0:
                return False

        return True

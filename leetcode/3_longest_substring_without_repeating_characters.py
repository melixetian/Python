"""
LC 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = set()
        left, res = 0, 0

        for right, ch in enumerate(s):
            while ch in mem:
                left_ch = s[left]
                mem.remove(left_ch)
                left += 1
            mem.add(ch)

            res = max(right - left + 1, res)

        return res

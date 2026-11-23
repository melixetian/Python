"""
LC 300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Найдите длину максимальной строго возрастающей подпоследовательности.
"""

from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # tails[i] — минимальный последний элемент подпоследовательности длины i + 1.
        tails = []
        for num in nums:
            index = bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num
        return len(tails)

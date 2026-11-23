"""
LC 35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = 0
        n = len(nums)
        while i < n and nums[i] < target:
            i += 1

        return i

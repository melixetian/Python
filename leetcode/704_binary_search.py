"""
LC 704. Binary Search
https://leetcode.com/problems/binary-search/
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid

        return left if nums[left] == target else -1

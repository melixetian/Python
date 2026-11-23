"""
LC 80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        write = 2
        for read in range(2, n):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write

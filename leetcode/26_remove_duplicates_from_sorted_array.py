"""
LC 26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        write = 1
        for read in range(1, n):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1

        return write

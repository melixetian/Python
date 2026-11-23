"""
LC 189. Rotate Array
https://leetcode.com/problems/rotate-array/
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        r = n - k
        stored = nums[:r]

        i = 0
        for j in range(n - k, n):
            nums[i] = nums[j]
            i += 1

        for j in range(n - k):
            nums[i] = stored[j]
            i += 1

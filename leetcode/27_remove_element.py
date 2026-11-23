"""
LC 27. Remove Element
https://leetcode.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """Remove element from list."""
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                while nums[right] == val:
                    right -= 1
                    if right <= left:
                        return left
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            left += 1

        return left

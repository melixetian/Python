"""
LC 169. Majority Element
https://leetcode.com/problems/majority-element/
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

"""
LC 228. Summary Ranges
https://leetcode.com/problems/summary-ranges/

Свернуть последовательные числа из отсортированного массива в диапазоны.
Вернуть список строк вида "a->b" для диапазонов и "a" для одиночных чисел.
"""


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = []
        start = 0

        while start < len(nums):
            end = start
            while end + 1 < len(nums) and nums[end + 1] == nums[end] + 1:
                end += 1

            if start == end:
                ranges.append(str(nums[start]))
            else:
                ranges.append(f"{nums[start]}->{nums[end]}")
            start = end + 1

        return ranges

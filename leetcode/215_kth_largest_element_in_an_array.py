"""
LC 215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

from heapq import heapify, heappushpop


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)  # O(k)

        for i in range(k, len(nums)):
            heappushpop(heap, nums[i])

        return heap[0]

"""
LC 703. Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""

from heapq import heapify, heappop, heappush


class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        self.k = k
        self.heap = nums
        heapify(self.heap)

        while len(self.heap) > self.k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)

        if len(self.heap) > self.k:
            heappop(self.heap)

        return self.heap[0]

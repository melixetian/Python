"""
LC 88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()

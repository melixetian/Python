"""
LC 21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    # При запуске решения ListNode предоставляет LeetCode.
    class ListNode:
        def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
            self.val = val
            self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional["ListNode"], list2: Optional["ListNode"]) -> Optional["ListNode"]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2

        return head.next

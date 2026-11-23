"""
LC 82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    # При запуске решения ListNode предоставляет LeetCode.
    class ListNode:
        def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
            self.val = val
            self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if not head or not head.next:
            return head

        base = ListNode(0, head)
        result = base
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicate = curr.val
                while curr and curr.val == duplicate:
                    curr = curr.next
                result.next = curr
            else:
                result = curr
                curr = curr.next

        return base.next

"""
LC 83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
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
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

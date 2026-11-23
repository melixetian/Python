"""
LC 141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    # При запуске решения ListNode предоставляет LeetCode.
    class ListNode:
        def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
            self.val = val
            self.next = next


class Solution:
    def hasCycle(self, head: Optional["ListNode"]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

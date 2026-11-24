"""
LC 141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

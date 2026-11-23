"""
LC 2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    # При запуске решения ListNode предоставляет LeetCode.
    class ListNode:
        def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
            self.val = val
            self.next = next


class Solution:
    def addTwoNumbers(self, l1: "ListNode", l2: "ListNode") -> "ListNode":
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 or l2 or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            res = digit1 + digit2 + carry
            digit = res % 10
            carry = res // 10

            tail.next = ListNode(digit)
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result

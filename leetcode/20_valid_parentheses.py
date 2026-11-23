"""
LC 20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Проверить правильность расстановки круглых, квадратных и фигурных скобок.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for bracket in s:
            opening = pairs.get(bracket)
            if opening is None:
                stack.append(bracket)
            elif not stack or stack.pop() != opening:
                return False

        return not stack

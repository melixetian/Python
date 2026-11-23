"""
LC 22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def generate(opened: int, closed: int, prefix: str) -> None:
            if opened == closed == n:
                result.append(prefix)
                return
            if opened < n:
                generate(opened + 1, closed, prefix + "(")
            if closed < opened:
                generate(opened, closed + 1, prefix + ")")

        generate(0, 0, "")
        return result

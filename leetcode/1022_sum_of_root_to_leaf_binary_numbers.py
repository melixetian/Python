"""
LC 1022. Sum of Root To Leaf Binary Numbers
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
"""

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    # При запуске решения TreeNode предоставляет LeetCode.
    class TreeNode:
        def __init__(
            self,
            val: int = 0,
            left: Optional["TreeNode"] = None,
            right: Optional["TreeNode"] = None,
        ) -> None:
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def sumRootToLeaf(self, root: "TreeNode") -> int:

        def dfs(node: "TreeNode", n=0) -> None:
            if not node:
                return

            n = 2 * n + node.val
            if not node.left and not node.right:
                self.ans += n
                return

            dfs(node.left, n)
            dfs(node.right, n)
            return

        self.ans = 0
        dfs(root)

        return self.ans

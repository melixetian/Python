"""
LC 104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Глубина дерева - число узлов на самом длинном пути от корня до листа.
Для пустого дерева глубина равна 0.
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
    def maxDepth(self, root: Optional["TreeNode"]) -> int:
        """Итеративный DFS: O(n) времени, O(h) дополнительной памяти."""
        if root is None:
            return 0

        max_depth = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))

        return max_depth

"""
LC 2196. Create Binary Tree From Descriptions
https://leetcode.com/problems/create-binary-tree-from-descriptions/

Каждая запись [parent, child, isLeft] описывает связь родителя и ребёнка.
Если isLeft == 1, ребёнок левый, иначе — правый.
Нужно построить бинарное дерево и вернуть его корень.
По условию описания непустые и задают корректное дерево с уникальными значениями.

Время — O(n) в среднем, память — O(n), где n — число описаний.
"""

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        nodes = {}
        children = set()

        for parent_val, child_val, is_left in descriptions:
            # Один объект на каждое значение, независимо от порядка описаний.
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)

            parent = nodes[parent_val]
            child = nodes[child_val]

            if is_left:
                parent.left = child
            else:
                parent.right = child

            children.add(child_val)

        # Корень — единственный узел, который не является чьим-либо ребёнком.
        root_val = next(val for val in nodes if val not in children)
        return nodes[root_val]

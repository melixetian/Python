"""
LC 133. Clone Graph
https://leetcode.com/problems/clone-graph/

Построить глубокую копию связного неориентированного графа.
Каждый узел содержит значение val и список соседей neighbors.
Для пустого графа вернуть None.

Время — O(V + E), служебная память — O(V) без учёта копии графа.
"""


class Node:
    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if node is None:
            return None

        old_to_new = {}

        def dfs(node: Node) -> Node:
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)

"""
LC 200. Number of Islands
https://leetcode.com/problems/number-of-islands/
"""

from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0":
                    continue
                if (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands

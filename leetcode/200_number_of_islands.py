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
        islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                        queue.append((r, c))
                        grid[r][c] = "0"

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1

        return islands

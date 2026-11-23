"""
LC 64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        dp = [0] * m
        dp[0] = grid[0][0]

        for j in range(1, m):
            dp[j] = dp[j - 1] + grid[0][j]

        for i in range(1, n):
            dp[0] += grid[i][0]
            for j in range(1, m):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[-1]

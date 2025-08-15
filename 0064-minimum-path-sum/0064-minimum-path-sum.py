# Solution 1: Bottom up DP (Space Optimized)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [float("inf")] * (COLS + 1)
        dp[COLS - 1] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[c] = grid[r][c] + min(dp[c], dp[c + 1])

        return dp[0]
# Time: O(M*N), Where m is the number of rows and n is the number of columns.
# Space: O(N)

"""
# Solution 2: Bottom up DP
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = [[float("inf")] * (COLS + 1) for r in range(ROWS + 1)]
        res[ROWS -1][COLS] = 0 # base case for bottom right

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS -1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        return res[0][0]
        
# Time: O(M*N), Where m is the number of rows and n is the number of columns.
# Space: O(M*N)
"""
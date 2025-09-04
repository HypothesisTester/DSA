class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0
        elif len(obstacleGrid) == 1:
            return 1 if 1 not in obstacleGrid[0] else 0

        self.memo = {}

        self.dfs(obstacleGrid, 0, 0)

        return self.memo[(0, 0)]

    def dfs(self, grid, m, n):
        if (m, n) in self.memo:
            return self.memo[(m, n)]

        if m == len(grid) - 1 and n == len(grid[m]) - 1:
            return 1
        
        if (0 <= m < len(grid)) and ( 0 <= n < len(grid[m])) and grid[m][n] == 0:
            self.memo[(m, n)] = self.dfs(grid, m + 1, n) + self.dfs(grid, m, n + 1)
        else:
            self.memo[(m, n)] = 0

        return self.memo[(m, n)]
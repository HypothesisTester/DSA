class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # out of bounds or water
            if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                return 0
            grid[r][c] = 0           # mark visited
            # count this cell + neighbors
            return (1
                  + dfs(r, c+1)
                  + dfs(r+1, c)
                  + dfs(r, c-1)
                  + dfs(r-1, c))

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area

# Time: O(rows * cols)
# Space: O(rows * cols)  (recursion stack)
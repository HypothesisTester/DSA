# Solution 1 — Dynamic Programming (Memoization)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.memo = {}
        
        self.directions = [(1,0), (0,1), (0, -1), (-1, 0)]

        res = 1

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                res = max(res, self.dfs(matrix, row, col))
        return res

    def dfs(self, matrix, cur_row, cur_col):
        if (cur_row, cur_col) in self.memo:
            return self.memo[(cur_row, cur_col)]

        self.memo[(cur_row, cur_col)] = 1

        for row_inc, col_inc in self.directions:
            new_row = cur_row + row_inc
            new_col = cur_col + col_inc

            if (0 <= new_row < len(matrix)) and (0 <= new_col < len(matrix[0])) and matrix[cur_row][cur_col] < matrix[new_row][new_col]:
                self.memo[(cur_row, cur_col)] = max(self.memo[(cur_row, cur_col)], 1 + self.dfs(matrix, new_row, new_col))

        return self.memo[cur_row, cur_col]

# Time: O(M*N)
# Space: O(M*N)
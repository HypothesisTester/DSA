class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = [[0] * ROWS for _ in range(COLS)] # New (blank) col x row matrix

        for r in range(ROWS):
            for c in range(COLS):
                res[c][r] = matrix[r][c]

        return res

# Time: O(M * N) - We visit every element once.
# Space: O(M * N) - We create a new M x N matrix.
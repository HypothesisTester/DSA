# Solution: Prefix Sums
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        # sumMat[i][j] = sum of matrix[0..i-1][0..j-1]
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # shift to 1-based indices in sumMat
        r1, c1 = row1 + 1, col1 + 1
        r2, c2 = row2 + 1, col2 + 1

        br = self.sumMat[r2][c2]            # bottom-right
        ab = self.sumMat[r1 - 1][c2]        # above region
        lf = self.sumMat[r2][c1 - 1]        # left region
        tl = self.sumMat[r1 - 1][c1 - 1]    # overlap

        return br - ab - lf + tl            # inclusion-exclusion

# Time: O(ROWS*COLS) init, O(1) per query  
# Space: O(ROWS*COLS)  



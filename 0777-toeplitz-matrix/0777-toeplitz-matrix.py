# Solution 1 — Diagonal-Start Sweep
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def is_diagonal_univalue(row, col):
            val = matrix[row][col]

            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != val:
                    return  False

                row += 1
                col += 1

            return True
        
        for col in range(len(matrix[0])):
            if not is_diagonal_univalue(0, col):
                return False

        for row in range(1, len(matrix)):
            if not is_diagonal_univalue(row, 0):
                return False

        return True

# Time: O(M*N)
# Space: O(1) if counting result as space, otherwise O(1)

"""
# Solution 2 — Adjacent Pair Check
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for row in range(len(matrix)-1):
            for col in range(len(matrix[0])-1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
        return True

# Time: O(M*N)
# Space: O(1)


# Solution 3 — Streaming Row-Shift Check 
def isToeplitz_stream(rows_iterable) -> bool:
    prev = None
    for row in rows_iterable:
        if prev is not None:
            for j in range(1, len(row)):
                if row[j] != prev[j-1]:
                    return False
        prev = row
    return True

# Time: O(M*N)
# Space: O(N)
"""
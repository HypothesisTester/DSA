class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])   # m = #rows, n = #cols
        left, right = 0, m * n - 1            # search over m*n virtual indices

        while left <= right:
            mid = (left + right) // 2
            row = mid // n                     # which row in 2D
            col = mid % n                      # which col in that row
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1                # search higher indices
            else:
                right = mid - 1               # search lower indices

        return False

# Time: O(log(m * n))
# Space: O(1)
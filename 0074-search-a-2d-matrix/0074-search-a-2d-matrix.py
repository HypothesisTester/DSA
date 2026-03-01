class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        row_index = -1

        while top <= bottom:
            mid_row = top + (bottom - top) // 2
            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][cols - 1]:
                top = mid_row + 1
            else:
                row_index = mid_row
                break

        if row_index == -1:
            return False

        low = 0
        high = cols - 1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

            



            

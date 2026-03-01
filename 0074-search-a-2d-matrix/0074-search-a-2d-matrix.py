class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        low = 0
        high = (rows * cols) - 1  # Total elements minus 1
        
        while low <= high:
            mid_idx = low + (high - low) // 2
            
            # --- THE TRICK ---
            r = mid_idx // cols
            c = mid_idx % cols
            # -----------------
            
            val = matrix[r][c]
            
            if val == target:
                return True
            if val < target:
                low = mid_idx + 1
            else:
                high = mid_idx - 1
                
        return False
            

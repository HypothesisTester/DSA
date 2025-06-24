class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows
        for row in range(9):
            seen = set()
            for col in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # validate columns
        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # validate 3×3 boxes
        starts = [(0,0), (0,3), (0,6),
                  (3,0), (3,3), (3,6),
                  (6,0), (6,3), (6,6)]
        for br, bc in starts:
            seen = set()
            for r in range(3):
                for c in range(3):
                    val = board[br + r][bc + c]
                    if val != '.':
                        if val in seen:
                            return False
                        seen.add(val)

        return True

# Time: O(1) on a fixed 9×9 board (O(N²) if generalised)
# Space: O(1) extra  


    
        

        
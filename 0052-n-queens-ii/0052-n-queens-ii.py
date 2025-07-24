class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        count = 0
        board = [["."] * n for i in range(n)] # dot means empty location

        def backtrack(r):
            if r == n:
                nonlocal count 
                count += 1
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue # Next position until valid

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"   
                
                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."  

        backtrack(0)
        return count

# Time: O(N!)
# Space: O(N)
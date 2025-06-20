class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # try each starting cell
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.dfs(board, row, col, word):
                        return True
        return False

    def dfs(self, board, row, col, word):
        # no more chars → match!
        if not word:
            return True
        # in bounds, not visited, and first char matches
        if (
            0 <= row < len(board)
            and 0 <= col < len(board[0])
            and board[row][col] != "#"
            and board[row][col] == word[0]
        ):
            placeholder = board[row][col] 
            board[row][col] = "#"   # mark visited

            # explore neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if self.dfs(board, row + dr, col + dc, word[1:]):
                    return True
            
            board[row][col] = placeholder   # restore
            return False

# Time: O(rows * cols * 4^L) worst-case, L = len(word)
# Space: O(L) recursion depth

# Note: Solution assumes you can overwrite board, if interviewer says you can't do this, you're going to need to maintain a visited set and use that to check whether or not you've been somewhere before, by maintaining tuple pairs of rows and columns to indicate whether or not you've been somewhere. You will have to undo the visited set so you're going to have to pop elements as you bubble up the recursion to ensure subsequent dfs's from a different start pos don't have that visited state.
        
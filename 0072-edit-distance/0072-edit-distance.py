# Solution: DP (top-down with memoization)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[float("inf")] * n for _ in range(m)]

        def dfs(i, j):
            # If word1 is exhausted, insert remaining word2
            if i == m:
                return n - j
            # If word2 is exhausted, delete remaining word1
            if j == n:
                return m - i
            
            if dp[i][j] != float("inf"):
                return dp[i][j]
            
            # If characters match, move to next
            if word1[i] == word2[j]:
                dp[i][j] = dfs(i + 1, j + 1)
            # Otherwise, try all operations
            else:
                insert = 1 + dfs(i, j + 1) 
                delete = 1 + dfs(i + 1, j)
                replace = 1 + dfs(i + 1, j + 1)

                dp[i][j] = min(insert, delete, replace)
            return dp[i][j]

        return dfs(0, 0)

# Time: O(m*n)
# Space: O(m*n) for dp + O(m+n) recursion stack

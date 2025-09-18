# Solution: Top Down DP (Memo)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubseq(s, s[::-1])

    def longestCommonSubseq(self, s1: str, s2: str) -> int:
        M, N = len(s1), len(s2)
        dp = [[0] * (N+1) for _ in range(M+1)]

        for i in range(M):
            for j in range(N):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[M][N]

# Time:  O(m * n) -> O(n^2)
# Space: O(m * n) -> O(n^2)

# Note: Realise to find LPS of a single string we need to just find the LCS of two strings (s, s[::-1])
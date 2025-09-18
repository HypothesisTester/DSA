# Solution 1: DP (tabulation) — forward fill on prefixes
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # dp[i][j] = LCS length of text1[:i] and text2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    # take best by skipping one char from either prefix
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[m][n]

# Time:  O(m * n)
# Space: O(m * n)

"""
# Solution 2: Top Down DP (Memo)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        @cache
        def longest(i, j):
            if i == m or j == n:
                return 0
            elif text1[i] == text2[j]:
                 return 1 + longest(i+1, j+1)
            else:
                return max(longest(i, j + 1), longest(i+1, j))

        return longest(0, 0)

# Time:  O(m * n)
# Space: O(m * n)
"""
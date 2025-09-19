# Solution: DP (Memo)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = {} # memo: dp[(i, j)] = # of subsequences of s[i:] that equal t[j:]

        def dfs(i, j): 
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                dp[(i, j)] = dfs(i + 1, j)
            return dp[(i, j)]

        return dfs(0, 0)

# Time:  O(len(s) * len(t))
# Space: O(len(s) * len(t))


            
        
# Solution: Dynamic Programming (Bottom-Up)
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1) # dp list for max product
        dp[1] = 1 # base case

        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                dp[num] = max(dp[num], dp[i] * dp[num - i])

        return dp[n]
    
# Time: O(n^2)
# Space: O(n)
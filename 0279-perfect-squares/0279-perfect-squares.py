class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, int(n**0.5) + 1)] # precompute squares
        dp = [n] * (n + 1) # dp list, safe base case n for each dp[i]
        dp[0] = 0

        for target in range(1, n + 1):
            for square in squares:
                if square > target:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        return dp[n]
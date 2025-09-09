# Solution 1: DP (Unbounded Knapsack space optimized)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[x] = number of ways to make sum x
        dp = [0] * (amount + 1)
        dp[0] = 1 # one way to make 0: choose nothing

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]   # extend ways to make (a - coin)

        return dp[amount]

# Note: Permutation version follow up -> amounts outer loop (1 to amount + 1), coins inner loop.

# Time: O(amount * len(coins))
# Space: O(amount)

"""
# Solution 2: Recursion (Memoisation)
# At each step: either take coin[i] again (stay on i) or skip to next coin (i+1)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, a):
            if a == amount:
                return 1
            
            if a > amount:
                return 0

            if i == len(coins):
                return 0

            if (i,a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        return dfs(0,0)

# Time: O(amount * len(coins))
# Space: O(amount * len(coins))
"""
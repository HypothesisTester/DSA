# Solution: Dynamic Programming (Top-Down)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {} # key=(i, buying) val=max_profit

        def dfs(i, canbuy):
            if i >= len(prices):
                return 0
            if (i, canbuy) in dp:
                return dp[(i, canbuy)]
            
            if canbuy:
                buy = dfs(i + 1, not canbuy) - prices[i]
                cooldown = dfs(i + 1, canbuy)
                dp[(i, canbuy)] = max(buy, cooldown)
            

            else:
                sell = dfs(i + 2, not canbuy) + prices[i]
                cooldown = dfs(i + 1, canbuy)
                dp[(i, canbuy)] = max(sell, cooldown)
            return dp[(i, canbuy)]

        return dfs(0, True)

# Time: O(1)
# Space: O(1)
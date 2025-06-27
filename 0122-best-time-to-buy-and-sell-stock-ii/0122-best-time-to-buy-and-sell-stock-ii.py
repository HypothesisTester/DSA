class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i -1]:
                profit += (prices[i] - prices[i -1])

        return profit

# Time: O(n) — single pass through prices
# Space: O(1) 

# Note: summing each local rise across a continuous upward segment always equals (or exceeds) the net gain from its start to end,so capturing every positive daily difference is optimal.
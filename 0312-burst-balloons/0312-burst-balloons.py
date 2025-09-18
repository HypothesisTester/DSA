class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad with 1's so the edge multiplications are uniform
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs (i + 1, r)
                # running max for [l..r]: best over all choices of 'i' as last
                dp[(l, r)] = max(dp[(l, r)], coins) 
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)

# Time: O(N^3) - N^2 intervals by N subintervals
# Space: O(N^2) - N^2 intervals

# Note: Fix the last balloon i in an interval [l..r]; this splits the problem into two independent subintervals [l..i-1] and [i+1..r]. Memoize each interval’s best result in dp[(l, r)].
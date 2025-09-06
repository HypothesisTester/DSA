# Solution 1: DP (Bottom  Up)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1 # (0 sum) -> 1 way

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp

        return dp[target]

# Time: O(N*SUM OF NUMS)
# Space: O(SUM OF NUMS)

"""
# Solution 2: DP (Memo)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {} # (index, cur_sum)
        def backtrack(i, cur_sum):
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]

            if i == len(nums):
                return 1 if cur_sum == target else 0

            dp[(i, cur_sum)] = (
                backtrack(i + 1, cur_sum + nums[i]) +
                backtrack(i + 1, cur_sum - nums[i])
            )
            return dp[(i, cur_sum)]

        return backtrack(0, 0)

# Time: O(N*SUM OF NUMS)
# Space: O(N*SUM OF NUMS)
"""
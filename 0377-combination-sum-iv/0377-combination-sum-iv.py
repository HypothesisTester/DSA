# Solution: DP (Bottom-Up)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = { 0 : 1 }
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
              dp[total] += dp.get(total - n, 0) # .get returns the value for key if present, otherwise returns default (here 0).

        return dp[target]

# Time:  O(target * len(nums))   # for each total we try every number
# Space: O(target)               # dp stores results for totals 0..target
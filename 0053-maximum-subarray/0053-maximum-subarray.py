# Solution: Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0                   # reset if negative
            curSum += num                   # extend current subarray
            maxSum = max(maxSum, curSum)   # track maximum
        return maxSum

# Time: O(n)
# Space: O(1)
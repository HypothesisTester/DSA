# Solution: Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = float("-inf")

        for num in nums:
            if num > curSum and curSum < 0:
                curSum = num
            else:
                curSum += num
            
            maxSum = max(maxSum, curSum)

        return maxSum
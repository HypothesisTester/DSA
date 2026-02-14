# Solution: Modified Kadane’s for circular array
# Time: O(n)
# Space: O(1)

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]
        curMax = globMax = nums[0]
        curMin = globMin = nums[0]

        for n in nums[1:]:
            # standard Kadane for max
            curMax = max(n, curMax + n)
            globMax = max(globMax, curMax)
            # inverted Kadane for min
            curMin = min(n, curMin + n)
            globMin = min(globMin, curMin)
            total += n

        # if all numbers negative, globMax is max element
        return max(globMax, total - globMin) if globMax > 0 else globMax
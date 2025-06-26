
# Solution 2: Hash Map
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        res = None
        maxCount = 0

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
            if counts[n] > maxCount:
                maxCount = counts[n]
                res = n

        return res
        
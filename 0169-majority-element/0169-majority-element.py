# Solution 1: Boyer-Moore Voting algorithim
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        # res is guaranteed to be the majority
        return res


# Time: O(N)
# Space: O(1)
"""
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

# Time: O(N)
# Space: O(N)
"""
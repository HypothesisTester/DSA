# Solution 1: Hash Map (One Pass) (Optimal)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # dict val, index

        for i, n in enumerate(nums): # Index, val
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i  # Stores num and index in dif

# Time: O(n)
# Space: O(n)


# Solution 2: Brute Force
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range (i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Time: O(n**2)
# Space: O(1)
"""
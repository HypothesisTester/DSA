# Solution 1: Hash Set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Time: O(n)
# Space: O(n)
        

"""
# Solution 2: Sorting

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

# Time: O(n logn)
# Space: O(1) or O(n) depepending on sorting algorithim
"""
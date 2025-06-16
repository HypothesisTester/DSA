# Solution 1: Sliding window
# Time: O(n), Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)          # up to two allowed

        left = 2                      # next write position
        for right in range(2, len(nums)):
            # keep nums[right] if not a third duplicate
            if nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1
        return left

        
"""
# Solution 2: Two pointers
# Time: O(n), Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1                        # write index
        count = 1                    # current run length

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1            # new value run

            if count <= 2:           # allow at most two
                nums[j] = nums[i]
                j += 1

        return j
"""
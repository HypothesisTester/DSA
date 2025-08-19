# Solution: Two Pointers
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0
        n = len(nums)
        while r < n:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

# Time: O(N)
# Space: O(1)
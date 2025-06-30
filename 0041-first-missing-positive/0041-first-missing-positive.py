class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 1) Place each value k in its “home” slot at index k-1
        for i in range(n):
            # keep swapping until nums[i] is either out of [1..n]
            # or already in the right spot
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                tgt = nums[i] - 1
                nums[i], nums[tgt] = nums[tgt], nums[i]
        
        # 2) The first index i whose slot i+1 isn’t there is our answer
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1
        
        # 3) All 1..n are present
        return n + 1

# Time: O(N)
# Space: O(1)
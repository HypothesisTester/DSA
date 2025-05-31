# BucketSort 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]           # count 0s, 1s, 2s

        for color in nums:
            counts[color] += 1
        
        R, W, B = counts

        nums[:R]     = [0] * R       # fill first R slots with 0
        nums[R:R+W]  = [1] * W       # next W slots with 1
        nums[R+W:]   = [2] * B       # remaining B slots with 2
        
        # Time: O(n)
        # Space: O(1)
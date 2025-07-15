class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        return max(
            self.rob_helper(nums[:-1]),
            self.rob_helper(nums[1:])
        )
    
    def rob_helper(self, nums):
        prev_house = 0
        two_houses_ago = 0

        for num in nums:
            best = max(num + two_houses_ago, prev_house)

            prev_house, two_houses_ago = best, prev_house

        return max(prev_house, two_houses_ago)

# Time: O(N)
# Space: O(1)
# Solution: Dynamic Programming (Hash Set)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: # odd -> false
            return False
        
        dp = {0} # base case
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False

# Time:  O(n * target / word_size) 
# Space: O(target) 
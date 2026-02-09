class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def can_jump_from(current_index):

            if current_index == len(nums) - 1:
                return True

            if current_index in memo:
                return memo[current_index]


            # max index from here
            furthest_jump = min(current_index + nums[current_index], len(nums) - 1)

            for next_index in range(furthest_jump, current_index, -1):
                
                # recursive
                if can_jump_from(next_index):
                    memo[current_index] = True
                    return True
            
            # dead end
            memo[current_index] = False
            return False
        
        return can_jump_from(0)

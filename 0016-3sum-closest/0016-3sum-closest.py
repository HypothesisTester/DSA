class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(n):
            lo = i + 1
            hi = n - 1
            while lo < hi:
                current_sum = nums[i] + nums[lo] + nums[hi]
                if abs(target-current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                if current_sum == target: 
                    break
                elif current_sum < target:
                    lo += 1
                else:
                    hi -= 1
        return closest_sum


        
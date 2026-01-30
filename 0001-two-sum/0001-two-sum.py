class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            cur_val = nums[i]

            remainder = target - cur_val

            if remainder in seen:
                return [seen[remainder], i]

            seen[cur_val] = i
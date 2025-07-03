class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            mid_val = nums[mid]

            if mid_val > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid - 1] > mid_val:
                return mid_val
            else:
                if mid_val > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
# Time: O(logN)
# Space: O(1)
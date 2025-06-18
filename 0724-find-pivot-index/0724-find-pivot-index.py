# Prefix Sums
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        globalsum = sum(nums)

        left_sum = 0

        for i, num in enumerate(nums):
            if globalsum - (2 * left_sum) == num:
                return i

            left_sum += num

        return -1

# Time: O(n)
# Space: O(1)
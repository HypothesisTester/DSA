class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2        # mid index
					 # Note: alternative to possibly avoid integer overflow is m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1           # search left half
            elif nums[m] < target:
                l = m + 1           # search right half
            else:
                return m            # found

        return -1                    # not found

# Time: O(log n)
# Space: O(1)
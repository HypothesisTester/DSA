class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # in case k > n

        def reverse_range(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # 1) reverse all, 2) reverse first k, 3) reverse remaining
        reverse_range(0, n - 1)
        reverse_range(0, k - 1)
        reverse_range(k, n - 1)

# Time: O(n)
# Space: O(1)
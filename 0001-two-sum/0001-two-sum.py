
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr = sorted((x, i) for i, x in enumerate(nums))
        l, r = 0, len(arr) - 1
        while l < r:
            s = arr[l][0] + arr[r][0]
            if s == target:
                return [arr[l][1], arr[r][1]]
            if s < target:
                l += 1
            else:
                r -= 1
# Two Pointers Solution

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1        # need smaller sum
            elif s < target:
                l += 1        # need larger sum
            else:
                return [l + 1, r + 1]  # 1-indexed result
        return []

# Time: O(n)
# Space: O(1)

# Solution: Two Pointers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        max_area = 0

        while l < r:
            w = r - l # width
            h = min(height[l], height[r]) # limiting height
            a = w * h
            max_area = max(max_area, a)
            # move the smaller side inward
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

# Reason why this works is we've presorted it by the width, i.e begininng is the lowest and end is the max, so all we need to consider is the height, by keeping the bar that is higher.

# Time: O(n)
# Space: O(1)
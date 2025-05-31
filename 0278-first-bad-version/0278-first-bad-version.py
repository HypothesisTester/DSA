# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n                   # search range [1..n]

        while l < r:
            mid = (l + r) // 2        # midpoint
            if isBadVersion(mid):
                r = mid               # bad → first bad is ≤ mid
            else:
                l = mid + 1           # good → first bad is > mid
        
        return r                      # l == r == first bad

# Time: O(log n)
# Space: O(1)
        
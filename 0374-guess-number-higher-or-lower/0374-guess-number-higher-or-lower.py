class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n                   # search range [l..r]

        while l <= r:
            m = (l + r) // 2          # mid-point guess
            res = guess(m)
            if res > 0:               # pick is higher
                l = m + 1
            elif res < 0:             # pick is lower
                r = m - 1
            else:
                return m              # found

# Time: O(log n)
# Space: O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)         # speed between 1 and max pile

        while left < right:
            mid = (left + right) // 2       # test speed = mid
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid) # compute hours at speed mid

            if hours <= h:
                right = mid                 # mid works, search lower
            else:
                left = mid + 1              # mid too slow, search higher

        return left  # left == right, smallest workable speed

# Time: O(n log M), where M = max(piles)
# Space: O(1)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() # Sort intervals by start (then by end as tiebreaker)

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                 # *overlap, we must remove one of the two
                res += 1
                # keep the one that ends *earliest* "greedy" solution
                prevEnd = min(prevEnd, end)
        return res

# Time: O(N log N)
# Space: O(N)
        
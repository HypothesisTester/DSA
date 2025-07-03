class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2

            if self.can_ship(mid, weights, days):
                r = mid
            else:
                l = mid + 1 
            
        return r
       
    def can_ship(self, candidate, weights, days):
        cur_weight = 0
        days_taken = 1

        for weight in weights:
            cur_weight += weight

            if cur_weight > candidate:
                days_taken += 1
                cur_weight = weight

        return days_taken <= days

# Time: O(NlogN)
# Space: O(1)

# Binary-search pattern notes:
#
# 1) Use `while l < r` when you’re searching for a bound (min or max)
#    rather than checking for existence.  This loop narrows [l, r]
#    until they meet at the answer.
#
# 2) Compute mid = (l + r) // 2 for the “lower‐bound” intent:
#      - If mid works (can_ship → True), keep it: r = mid
#      - Else discard mid:           l = mid + 1
#
# 3) Don’t do r = mid – 1 here, because mid itself may be the minimal
#    valid capacity.  Stepping past it would skip the true answer.
#
# 4) If you instead need to search *inside* a concrete array for a value,
#    you’d typically use `while l <= r` and return from within the loop
#    when you find it (and adjust to `l = mid + 1` or `r = mid – 1`).
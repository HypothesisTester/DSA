# Solution 1: HashSet "Sliding Window" approach

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()   # holds the current sliding window’s values
        L = 0            # left boundary of the window

        for R in range(len(nums)):      # R is the right boundary, we expand one at a time
            # If our window size would exceed k+1, shrink it from the left:
            if R - L > k:
                window.remove(nums[L])
                L += 1

            # Now check if nums[R] is already in the window:
            if nums[R] in window:
                return True            # found a duplicate within distance k

            window.add(nums[R])      # otherwise add the new element and continue

        return False                   # no such pair found

# Time: O(n)
# Space: O(min(n,k))

"""
# Solution 2: Hashmap, store num → last index
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_i = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in num_to_i:
                if abs(num_to_i[nums[i]] - i) <= k:
                    return True
            num_to_i[nums[i]] = i # update last seen index

        return False

# Time: O(n)
# Space: O(n)
"""
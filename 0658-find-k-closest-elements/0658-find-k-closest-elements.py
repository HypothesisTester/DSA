class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1

        # set pointers around insertion point
        l, r = l - 1, l

        # expand window until we have k elements
        while r - l - 1 < k:
            if l < 0:               # l out of bounds
                r += 1
            elif r >= len(arr):     # r out of bounds
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):  # left is closer (or tie)
                l -= 1
            else:                   # right is closer
                r += 1

        return arr[l + 1:r]  # Returns k closest elements from index l+1 to r-1

# Time: O(log n + k)
# Space: O(1) extra
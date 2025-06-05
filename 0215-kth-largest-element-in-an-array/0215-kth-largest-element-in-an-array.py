import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]       # build max-heap via negation
        heapq.heapify(nums)             # O(n)

        for _ in range(k - 1):
            heapq.heappop(nums)         # remove k-1 largest

        return -heapq.heappop(nums) # return k-th largest

# Time: O(n + k log n)
# Space: O(n)
# Solution 1: Min Heap (Optimal)

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []                    # store k largest seen so far

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)     # fill until size k
            else:
                heapq.heappushpop(min_heap, num)  # replace smallest if num is larger
            
        return min_heap[0]               # root is kth largest

# Time: O(n log k)
# Space: O(k)
                

"""
# Solution 2: Max Heap

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]       # build max-heap via negation
        heapq.heapify(nums)             # O(n)

        for _ in range(k - 1):
            heapq.heappop(nums)         # remove k-1 largest

        return -heapq.heappop(nums) # return k-th largest

# Time: O(n + k log n)
# Space: O(n)
"""
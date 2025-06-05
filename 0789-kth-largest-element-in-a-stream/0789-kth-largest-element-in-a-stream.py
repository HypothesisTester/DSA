import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums                 # store up to k largest scores
        heapq.heapify(self.minHeap)         # build heap in O(n)
        # keep only k largest by popping smallest until size == k
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)    # add new score
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)      # remove smallest if more than k
        return self.minHeap[0]               # top is kth largest

# Time Complexity:
#   __init__: O(n + (n-k) log n) ≈ O(n log n) in worst case
#   add: O(log k)
# Space Complexity: O(k)
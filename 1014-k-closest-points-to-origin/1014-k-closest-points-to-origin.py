import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)                  # squared distance from origin
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)                # build min-heap by distance
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)  # pop closest point
            res.append([x, y])
            k -= 1

        return res

# Time: O(n + k log n)
# Space: O(n)
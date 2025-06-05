class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert to max-heap by negating
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: 
                # push the difference (negated)
                heapq.heappush(stones, first - second) 
        
        # if heap is empty, return 0; else return abs of remaining
        return abs(stones[0]) if stones else 0

# Time: O(n log n)
# Space: O(n)  
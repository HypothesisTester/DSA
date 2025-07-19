class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = "", []
        # seed heap with nonzero counts (negated for max-heap)
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

            
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            # avoid three in a row
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(maxHeap, (count, char))     
        return res

# Time: O(N) — each character appended once, heap ops are O(1)
# Space: O(1) — heap holds at most 3 elements, result string excluded
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        
        return len(good) == 3
        
# Time Complexity: O(m) where m = number of triplets (each checked in O(1))
# Space Complexity: O(1) extra (the 'good' set holds at most 3 elements)
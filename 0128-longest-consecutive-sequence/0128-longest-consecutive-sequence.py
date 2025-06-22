from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # map each unique number to an index for DSU
        unique = set(nums)
        idx = {num: i for i, num in enumerate(unique)}
        n = len(unique)

        parent = list(range(n))
        size   = [1] * n
        maxlen = 1

        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int) -> bool:
            nonlocal maxlen
            ri, rj = find(i), find(j)
            if ri == rj:
                return False
            if size[ri] < size[rj]:
                ri, rj = rj, ri
            parent[rj] = ri
            size[ri]  += size[rj]
            maxlen     = max(maxlen, size[ri])
            return True

        # union neighbors if both present
        for num in unique:
            i = idx[num]
            if num - 1 in idx:
                union(i, idx[num - 1])
            if num + 1 in idx:
                union(i, idx[num + 1])

        return maxlen  
        # Time: O(n α(n)), Space: O(n)
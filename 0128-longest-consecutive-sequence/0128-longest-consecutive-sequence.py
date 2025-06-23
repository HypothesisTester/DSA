# Solution 1: Hash Set (Optimal)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        # iterate unique numbers only to avoid re-scanning duplicates
        for num in s:
             # start a new sequence if num-1 isn't present
            if num - 1 not in s:
                length = 1
                next_num = num + 1
                 # count upwards while consecutive
                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest

# Time: O(n)
# Space: O(n)

"""
# Solution 2: Union Find
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

# Time: O(n α(n))
# Space: O(n)
"""
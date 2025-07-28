# Solution: Greedy (Simple bfs / two pointers)
class Solution:
    def jump(self, nums: List[int]) -> int:
        # res = jumps taken; [l..r] = current window of reachable indices
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            # scan current window for how far we can reach next
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1

        return res

# Time: O(n) — each index visited once
# Space: O(1) — only a few pointers and counters
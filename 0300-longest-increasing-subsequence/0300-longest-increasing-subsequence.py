# Solution: DP (Memo)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            best = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))
            dp[i] = best
            return best

        return max(dfs(i) for i in range(n))

# Time:  O(n^2)  — each i considers all j>i
# Space: O(n)    — cache has n entries; recursion depth ≤ n
        
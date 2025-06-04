class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:               # found valid combination
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return                         # out of bounds or overshot

            # include candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()                          # backtrack

            # skip to next candidate
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
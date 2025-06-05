class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def make_combination(idx, comb, total):
            if total == target:
                res.append(comb.copy())         # found valid combo
                return
            if total > target or idx >= len(candidates):
                return                         # overshoot or no more candidates

            # choose candidates[idx]
            comb.append(candidates[idx])
            make_combination(idx, comb, total + candidates[idx])
            comb.pop()                         # backtrack

            # skip to next candidate
            make_combination(idx + 1, comb, total)

        make_combination(0, [], 0)
        return res

# Time: O(2^n)  
# Space: O(n) (call stack + current combination)
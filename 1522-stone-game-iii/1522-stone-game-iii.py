# Solution: DP (Memo)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = {}  # dp[i] = best (current player's score − opponent's) starting at index i

        def dfs(i):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]

            best = float("-inf")
            take = 0
            for k in range(3):
                if i + k >= n:
                    break
                take += stoneValue[i + k]
                # net lead if we take k+1 stones now:
                # (we gain 'take') minus opponent's optimal lead on the rest
                cand = take - dfs(i + k + 1)
                best = max(best, cand) # keep the best of the 1/2/3 choices

            dp[i] = best
            return best

        diff = dfs(0) # overall best difference from start
        return "Alice" if diff > 0 else "Bob" if diff < 0 else "Tie"

# Time:  O(n) — each i is solved once; up to 3 transitions per state
# Space: O(n) — memo size O(n)
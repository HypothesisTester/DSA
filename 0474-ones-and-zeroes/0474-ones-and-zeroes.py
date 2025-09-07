class Solution:
    def findMaxForm(self, strs, m, n):
        counts = [(s.count('0'), s.count('1')) for s in strs]  # List[Tuple[int, int]]
        dp = {}  # memo: (i, m_left, n_left) -> best size

        def dfs(i, m_left, n_left):
            if i == len(strs):
                return 0
            key = (i, m_left, n_left)
            if key in dp:
                return dp[key]

            zeroes, ones = counts[i]  # precomputed counts for strs[i]
            best = dfs(i + 1, m_left, n_left)  # skip
            if zeroes <= m_left and ones <= n_left:  # take
                best = max(best, 1 + dfs(i + 1, m_left - zeroes, n_left - ones))

            dp[key] = best
            return best

        return dfs(0, m, n)

# Time:  O(L*M*N) after one-time O(total_chars) precompute for `counts`
# Space: O(L*M*N) memo + O(L) recursion stack
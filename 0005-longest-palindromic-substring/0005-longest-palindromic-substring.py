# Solution: Two Pointers
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        def expand(L, R):
            while L >= 0 and R < n and s[L] == s[R]:
                L -= 1
                R += 1
            return L+1, R-1  # inclusive bounds

        bestL = bestR = 0
        for i in range(n):
            l1, r1 = expand(i, i)       # odd length
            l2, r2 = expand(i, i+1)     # even length
            if r1 - l1 > bestR - bestL:
                bestL, bestR = l1, r1
            if r2 - l2 > bestR - bestL:
                bestL, bestR = l2, r2

        return s[bestL:bestR+1]

# Time: O(n^2) worst-case
# Space: O(1) extra
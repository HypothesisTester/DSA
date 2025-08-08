# Solution: Two Pointers
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def expand(L, R):
            cnt = 0
            while L >= 0 and R < n and s[L] == s[R]:
                cnt += 1    # +1 for each palindrome found during expansion
                L -= 1
                R += 1
            return cnt

        total = 0
        for i in range(n):
            total += expand(i, i)     # odd centers
            total += expand(i, i+1)   # even centers
        return total

# Time: O(n^2) worst-case
# Space: O(1) extra
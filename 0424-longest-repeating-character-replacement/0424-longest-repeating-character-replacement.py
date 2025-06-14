class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}     # freq of each letter in window
        res = 0
        l = 0
        maxf = 0       # max freq in window

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])     # update window’s top freq

            # if need more than k replacements, shrink window
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

# Time: O(n)
# Space: O(1)  (only 26 letters)
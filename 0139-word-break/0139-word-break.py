# Solution: Dynamic Programming (Bottom-Up)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

# Time: O(n∗m∗t)
# Space: O(n)

# Where n is the length of the string s,m is the number of words in wordDict and t is the maximum length of any word in wordDict.
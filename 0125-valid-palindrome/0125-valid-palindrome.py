# Solution 1: Two Pointers (Optimal)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not self.alphaNum(s[l]):     # skip left non-alnum
                l += 1
            elif not self.alphaNum(s[r]):   # skip right non-alnum
                r -= 1
            elif s[l].lower() == s[r].lower():  # match     
                l += 1
                r -= 1
            else:                            # mismatch
                return False
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

# Time: O(n), Space: O(1)



"""
# Solution 2: Reverse String
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

# Time: O(n), Space: O(n)
"""
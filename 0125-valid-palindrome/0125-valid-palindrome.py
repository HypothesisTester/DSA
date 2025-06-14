class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            # skip non-alphanumeric from left
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # skip non-alphanumeric from right
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # compare lowercase chars
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c: str) -> bool:
        o = ord(c)
        # A–Z, a–z, or 0–9
        return (65 <= o <= 90) or (97 <= o <= 122) or (48 <= o <= 57)

# Time: O(n)
# Space: O(1)
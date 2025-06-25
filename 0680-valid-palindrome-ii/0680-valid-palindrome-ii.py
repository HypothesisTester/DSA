class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(i: int, j: int) -> bool:
            # check s[i..j] is palindrome
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # try removing one char either from left or right
                return is_pal(l + 1, r) or is_pal(l, r - 1)
            l, r = l + 1, r - 1
        return True

# Time: O(n)
# Space: O(1)
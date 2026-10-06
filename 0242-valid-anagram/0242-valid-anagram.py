from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = defaultdict(int)
        for ch in s:
            counts[ch] += 1
        for ch in t:
            counts[ch] -= 1
            if counts[ch] < 0:
                return False
        return True
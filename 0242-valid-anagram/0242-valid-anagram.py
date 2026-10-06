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
        return all(c == 0 for c in counts.values())

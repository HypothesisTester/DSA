from collections import defaultdict
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res, occ, n = 0, defaultdict(int), len(s)
        for i in range(n - minSize + 1):
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                occ[sub] += 1
                res = max(res, occ[sub])
        return res
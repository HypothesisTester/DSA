# Solution: Greedy (Hashmap)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} # char -> last index in s

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res

# Time: O(N)
# Space: O(M)
# Note: n is the length of the string s, m is the number of unique characters in the string s

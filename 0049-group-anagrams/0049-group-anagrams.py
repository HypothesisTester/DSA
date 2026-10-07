from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for w in strs:
            groups["".join(sorted(w))].append(w)
        return list(groups.values())
        
        
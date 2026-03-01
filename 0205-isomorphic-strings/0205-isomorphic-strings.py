from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s = defaultdict(list)
        map_t = defaultdict(list)
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i ] 

            if char_s in map_s and map_s[char_s] != char_t:
                return False

            if char_t in map_t and map_t[char_t] != char_s:
                return False

            map_s[char_s] = char_t
            map_t[char_t] = char_s

        return True
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        groupsP = {}
        groupsW = {}
        
        for i in range(len(pattern)):
            p, w = pattern[i], words[i]
            
            if p not in groupsP:
                if w in groupsW:
                    return False
                groupsP[p] = w
                groupsW[w] = p
            else:
                if groupsP[p] != w or groupsW[w] != p:
                    return False
        
        return True
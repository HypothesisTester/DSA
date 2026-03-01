class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If they are isomorphic, the number of unique characters in s, 
        # the number of unique characters in t, and the number of 
        # unique PAIRS of characters must all be exactly the same.
        
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
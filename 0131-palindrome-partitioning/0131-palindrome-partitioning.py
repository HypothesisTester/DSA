# Solution 1: Backtracking
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1 , r - 1

        return True

# Time: O(n · 2ⁿ)
# Space: O(n)      
        
"""
# Solution 2: Backtracking
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def backtrack(start: int):
            if start == len(s):
                res.append(part.copy())
                return
            for end in range(start+1, len(s)+1):
                sub = s[start:end]
                if sub == sub[::-1]:            # palindrome test
                    part.append(sub)
                    backtrack(end)
                    part.pop()

        backtrack(0)
        return res

# Time: O(n · 2ⁿ)
# Space: O(n)   
"""
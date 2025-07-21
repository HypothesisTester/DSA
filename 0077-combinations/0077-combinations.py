# Solution: Backtracking
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, sol = [], []
       
        def backtrack(i):
            if len(sol) == k:
                result.append(sol[:])
                return 
            for num in range(i, n + 1):
                sol.append(num) # choose
                backtrack(num+1) # recurse
                sol.pop() # un-choose
        backtrack(1)
        return result

# Time: O(N choose K)
# Space: O(N)
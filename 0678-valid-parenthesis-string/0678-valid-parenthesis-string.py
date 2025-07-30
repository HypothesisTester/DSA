# Solution: Greedy (range‐tracking)
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0: # handles case where, s = (*)(
                leftMin = 0
        
        return leftMin == 0

# Time Complexity: O(n) — single pass through s  
# Space Complexity: O(1) — just a couple of counters  
        
# Iterative Solution

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]                  # start with the empty subset
        
        for num in nums:
            # for each existing subset, make a new one that also includes num
            for i in range(len(res)):
                res.append(res[i] + [num])
        
        return res
# Time O(2^n)
# Space O(n)


        
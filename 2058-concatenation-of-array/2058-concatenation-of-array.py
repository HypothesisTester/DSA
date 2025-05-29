class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for r in range(2):
            for n in nums:
                ans.append(n)
        return ans
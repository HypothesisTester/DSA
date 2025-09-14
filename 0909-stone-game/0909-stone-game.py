class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

# Mathematical solution: Alice can either pick every even pile or every odd pile. Sum all even piles != sum of all odd piles. One sum must be greater than the other. Alice will pick the maximum between the two so Alice will always win.
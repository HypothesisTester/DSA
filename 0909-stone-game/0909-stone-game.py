# Solution 1: Mathematical
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

# Time: O(1) 
# Space: O(1) 

# Mathematical solution: Alice can either pick every even pile or every odd pile. Sum all even piles != sum of all odd piles. One sum must be greater than the other. Alice will pick the maximum between the two so Alice will always win.

"""
# Solution 2: DP (Memo)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {} # subarr piles (l, r) -> Max Alice Total
        n = len(piles)
        
        # Return: Max Alice Total
        def dfs(l, r):
            if l > r:
                return 0 
            if (l, r) in dp:
                return dp[(l, r)]

            alice_turn = ((r - l + 1) % 2) == (n % 2)

            if alice_turn:
                # Alice's turn: she takes left or right; add stones now takes max
                best = max(dfs(l + 1, r) + piles[l],
                           dfs(l, r - 1) + piles[r])
            else:
                # Bob's turn: Alice gains 0 now; Bob minimizes Alice's eventual total.
                best = min(dfs(l + 1, r),
                           dfs(l, r - 1))

            dp[(l, r)] = best
            return best

        total = sum(piles)
        alice_score = dfs(0, n - 1)
        return alice_score > (total - alice_score)

# Time: O(n^2) 
# Space: O(n^2)
"""
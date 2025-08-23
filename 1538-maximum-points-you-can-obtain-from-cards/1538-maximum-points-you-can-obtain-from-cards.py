# Solution: Sliding Window (variant)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = cur = 0

        for i in range(-k, k):
            cur += cardPoints[i]

            if i >= 0:
                cur -= cardPoints[i - k]

            ans = max(cur, ans)
        
        return ans

# Time: O(K)
# Space: O(1)
        
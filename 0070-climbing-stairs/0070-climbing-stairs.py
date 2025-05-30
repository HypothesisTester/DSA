class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        cur = 2

        for _ in range(2, n):
            prev, cur = cur, prev + cur # fib-style update


        return cur

        # Time: O(1)
        # Space: O(1)


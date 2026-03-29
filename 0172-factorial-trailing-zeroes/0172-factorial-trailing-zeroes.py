class Solution:
    def trailingZeroes(self, n: int) -> int:
        numof5 = 0
        k = 1
        while 5**k <= n:
            numof5 += n // 5**k
            k += 1

        return numof5
        
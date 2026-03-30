class Solution:
    def trailingZeroes(self, n: int) -> int:
        numof5 = 0
        k = 1
        while 5**k <= n:
            numof5 += n // 5**k
            k += 1

        return numof5

# num of zeros = num of times 10 divides
# 10 can be factored into 2 * 5
# Take minimum of  num of 2 and num of 5 and their powers in n
# realise num of 5s will always be smaller so you can just find that
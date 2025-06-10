class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # shift left to make room for next bit
            res = res << 1

            # add the rightmost bit of n
            res = res | (n & 1)

            # shift the n to right to get the next bit
            n = n >> 1
        
        return res

# Time: O(1)   (always 32 iterations)
# Space: O(1)
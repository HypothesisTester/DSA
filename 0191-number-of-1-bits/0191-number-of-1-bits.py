class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1        # add lowest bit
            n >>= 1               # shift right
        return count

# Time: O(1)   (fixed 32/64-bit integer)
# Space: O(1)
# Soltion: Prefix Sum
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)     # prefix[i] = sum(nums[:i+1])

    def sumRange(self, left: int, right: int) -> int:
        # sum from 0..right minus sum from 0..left-1
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum

# Time: O(N) init, O(1) per query
# Space: O(N)
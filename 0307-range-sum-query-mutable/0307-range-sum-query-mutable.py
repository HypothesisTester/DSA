class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        self.nums = [0] * self.n

        for i, val in enumerate(nums):
            self.update(i, val)
        

    def _update(self, i: int, delta: int):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i) 

    def update(self, i: int, val: int):
        delta = val - self.nums[i]
        self.nums[i] = val
        self._update(i, delta)

    def _prefix_sum(self, i: int) -> int:
        i += 1
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self._prefix_sum(right)
        return self._prefix_sum(right) - self._prefix_sum(left - 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
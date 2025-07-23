class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k

        nums.sort(reverse=True)
        if nums[0] > target:          # largest stick too big
            return False

        used = [False] * len(nums)

        def backtrack(start: int, k_remain: int, subset_sum: int) -> bool:
            # if only one bucket left, it must work
            if k_remain == 1:
                return True
            # filled one bucket, move to next
            if subset_sum == target:
                return backtrack(0, k_remain - 1, 0)

            prev = -1
            for i in range(start, len(nums)):
                # skip used, overflow, or duplicate at this level
                if used[i] or subset_sum + nums[i] > target or nums[i] == prev:
                    continue

                used[i] = True
                if backtrack(i + 1, k_remain, subset_sum + nums[i]):
                    return True
                used[i] = False

                prev = nums[i]
                # if we fail on an empty bucket, no need to try further
                if subset_sum == 0:
                    break

            return False

        return backtrack(0, k, 0)

# Time: O(k * 2^n) worst‐case, but heavy pruning makes it much faster in practice
# Space: O(n) recursion depth + O(n) for `used[]`
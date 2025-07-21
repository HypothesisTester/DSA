class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, subset = [], []

        def backtrack(start: int):
            # record current subset
            result.append(subset.copy())

            for i in range(start, len(nums)):
                # skip duplicates at this decision level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])   # choose
                backtrack(i + 1)         # recurse
                subset.pop()             # un-choose

        backtrack(0)
        return result

# Time: O(2^n) — each element has two choices (in/out)
# Space: O(n)   — recursion depth and subset copy size
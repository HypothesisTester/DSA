# Solution: Boyer Moore's algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            # only cancel votes when we have 3 distinct keys
            if len(count) > 2:
                new_count = defaultdict(int)
                for k, c in count.items():
                    if c > 1:
                        new_count[k] = c - 1
                count = new_count

        # final check: only 0, 1, or 2 keys remain
        res = []
        for k in count:
            if nums.count(k) > len(nums) // 3:
                res.append(k)
        return res

# Time: O(n) — single pass + O(1) extra scans for candidates
# Space: O(1) — dict holds at most two keys and a small result list
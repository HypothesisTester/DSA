# Solution: Prefix Sums and Dictionary
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_dict = defaultdict(int)
        prefix_dict[0] = 1            # base case: sum 0 has one count
        prefix_sum = res = 0

        for num in nums:
            prefix_sum += num
            # any prior prefix_sum of (current–k) yields a subarray == k
            res += prefix_dict[prefix_sum - k]
            prefix_dict[prefix_sum] += 1

        return res

# Time: O(n)
# Space: O(n)
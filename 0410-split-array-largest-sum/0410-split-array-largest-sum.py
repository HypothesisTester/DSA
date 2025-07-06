class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        while l <= r:
            candidate_sum = (l + r) // 2

            if self.min_subarrays_required(nums, candidate_sum) <= k:
                r = candidate_sum - 1
                ans = candidate_sum
            else:
                l = candidate_sum + 1
            
        return ans

    def min_subarrays_required(self, nums, candidate_sum):
        cur_sum = 0
        subarrays = 1

        for num in nums:
            if cur_sum + num <= candidate_sum:
                cur_sum += num
            else:
                cur_sum = num

                subarrays += 1

        return subarrays

# Time: O(N log S), where S is search space
# Space: O(1)
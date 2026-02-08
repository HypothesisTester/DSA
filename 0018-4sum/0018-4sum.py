class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def kSum(k, start, target):
            res = []

            # base case k = 2
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    curr_sum = nums[l] + nums[r]
                    if curr_sum == target:
                        res.append([nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]: # skip duplicates
                            l += 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        r -= 1
                return res

            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i-1]:
                    continue

                sub_results = kSum(k-1, i + 1, target - nums[i])

                for subset in sub_results:
                    res.append([nums[i]] + subset)

            return res

        return kSum(4, 0, target)
        
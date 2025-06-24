class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            # since array is sorted, no need to proceed if nums[i] > 0
            if nums[i] > 0:
                break
            # skip duplicate i values
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i+1, n-1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    # skip duplicates for lo
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    # skip duplicates for hi
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif total < 0:
                    lo += 1    # need a larger sum
                else:
                    hi -= 1    # need a smaller sum

        return answer

# Time: O(n²)
# Space: O(1) extra (ignoring output)
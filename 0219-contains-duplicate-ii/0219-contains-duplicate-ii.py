class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}

        for index_j in range(len(nums)):
            numj = nums[index_j]
            if numj in dict:
                index_i = dict[numj]

                if abs(index_i - index_j) <= k:
                    return True

                dict[numj] = index_j
            
            else:
                dict[numj] = index_j
        return False
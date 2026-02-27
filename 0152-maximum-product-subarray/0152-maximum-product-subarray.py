class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_prod = max(nums)

        islands = []
        current_island = []
        for x in nums:
            if x == 0:
                if current_island:
                    islands.append(current_island)
                current_island = []
            else:
                current_island.append(x)
        if current_island:
            islands.append(current_island)
        
        for arr in islands:
            curr = 1

            for x in arr:
                curr *= x
                max_prod = max(max_prod, curr)

            curr = 1
            for x in reversed(arr):
                curr *= x
                max_prod = max(max_prod, curr)

        return max_prod

            

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]  # indices 0…len(nums)

        for n in nums:
            # get current count or 0 if missing, then +1
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():  # number, frequency
            freq[c].append(n)       # bucket numbers by frequency

        res = []
        # scan from highest freq down to 1
        for f in range(len(freq) - 1, 0, -1):
            for n in freq[f]:        
                res.append(n)
                if len(res) == k:    
                    return res

# Time: O(N)
# Space: O(N)
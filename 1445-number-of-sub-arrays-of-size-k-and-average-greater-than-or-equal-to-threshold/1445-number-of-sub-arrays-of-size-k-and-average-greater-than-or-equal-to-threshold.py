class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k-1])            # sum of first k-1 elements

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]       # include the kᵗʰ element
            if (curSum / k) >= threshold:   # compare 
                res += 1
            curSum -= arr[L]               # remove the leftmost element
        return res

# Time: O(n)
# Space: O(1)
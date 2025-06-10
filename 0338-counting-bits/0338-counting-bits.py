class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)            # ans[0] = 0
        for i in range(1, n + 1):
            # drop LSB, then add 1 if LSB was set
            ans[i] = ans[i >> 1] + (i & 1)
        return ans

# Time: O(n)   (one constant‐time step per i)
# Space: O(n)  (output array of size n+1)

"""
Explanation
We build an array ans where each ans[i] is the bit‐count of i.  Notice:
	•	Shifting i right by one (i>>1) drops its least‐significant bit, so ans[i>>1] is the count of all but that bit.
	•	i & 1 is 1 if the dropped bit was 1, else 0.

Hence

ans[i] = ans[i>>1] + (i & 1)
"""
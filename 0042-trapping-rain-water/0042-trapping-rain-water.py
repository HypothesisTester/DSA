# Solution: Two Pointers / Greedy

class Solution:
    def trap(self, height: List[int]) -> int:
        l = trapped = 0
        r = len(height) - 1
        l_max = r_max = 0

        while l < r:
            cl, cr = height[l], height[r]
            l_max = max(l_max, cl)     # update left max
            r_max = max(r_max, cr)     # update right max

            if l_max < r_max:
                trapped += l_max - cl  # trap at left
                l += 1
            else:
                trapped += r_max - cr  # trap at right
                r -= 1

        return trapped

# Time: O(n), Space: O(1)
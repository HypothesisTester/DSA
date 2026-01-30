class Solution:
    def trap(self, height: List[int]) -> int:
        l = trapped = 0
        r = len(height) - 1

        l_max = r_max = 0

        while l < r:
            cur_l = height[l]
            cur_r = height[r]

            l_max = max(l_max, cur_l)
            r_max = max(r_max, cur_r)

            if l_max < r_max:
                trapped += l_max - cur_l
                l += 1

            else:
                trapped += r_max - cur_r
                r -= 1
        return trapped


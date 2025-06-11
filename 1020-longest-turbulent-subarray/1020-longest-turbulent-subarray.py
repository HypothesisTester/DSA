# Sliding Window Solution

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, res, prev = 0, 1, 1, ""   # window [l..r), prev stores last comp

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">": # expecting '>'
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":   # expecting '<'
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                # reset window if equal, else slide to new start
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""

        return res

# Time: O(n)
# Space: O(1)
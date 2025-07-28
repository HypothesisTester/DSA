# Solution: Greedy (BFS)
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q = deque([0])               # positions we can “jump from”
        farthest = 0                 

        while q:
            i = q.popleft()

            # next valid jump targets lie in [i+minJump … i+maxJump],
            # but anything ≤ farthest has already been considered
            start = max(i + minJump, farthest + 1)
            end   = min(i + maxJump, n - 1)

            for j in range(start, end + 1):
                if s[j] == '0':
                    if j == n - 1:
                        return True    # reached the last index!
                    q.append(j)

            farthest = max(farthest, end)

        return False                  # queue exhausted without success

# Time:  O(n) — each index is enqueued & processed at most once  
# Space: O(n) — the queue can hold up to n indices in the worst case  
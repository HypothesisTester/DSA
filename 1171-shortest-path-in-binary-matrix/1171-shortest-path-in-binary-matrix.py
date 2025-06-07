from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # start or end blocked?
        if grid[0][0] or grid[N-1][N-1]:
            return -1

        q = deque([(0, 0, 1)])      # r, c, path length
        visit = {(0, 0)}            # visited cells
        direct = [(0,1),(1,0),(0,-1),(-1,0),
                  (1,1),(-1,-1),(1,-1),(-1,1)]

        while q:
            r, c, length = q.popleft()
            # skip out-of-bounds or water
            if min(r, c) < 0 or max(r, c) >= N or grid[r][c]:
                continue
            if r == N-1 and c == N-1:  # reached end
                return length

            for dr, dc in direct:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visit:
                    visit.add((nr, nc))
                    q.append((nr, nc, length + 1))

        return -1

# Time: O(N²) — each cell enqueued once
# Space: O(N²) — queue + visited set
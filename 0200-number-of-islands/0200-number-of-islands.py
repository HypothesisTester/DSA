import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()                   # seen land cells
        islands = 0
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(r, c):
            q = collections.deque([(r, c)])
            visited.add((r, c))
            while q:
                cr, cc = q.popleft()            # current cell
                for dr, dc in DIRECTIONS:      # neighbor offsets
                    nr, nc = cr + dr, cc + dc
                    # in bounds, is land, not visited
                    if (nr in range(rows) 
                        and nc in range(cols)
                        and grid[nr][nc] == "1" 
                        and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                # found new island
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands

# Time: O(rows * cols)
# Space: O(rows * cols) — worst-case queue/visited size
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        p_que, p_seen = deque(), set()
        a_que, a_seen = deque(), set()

        # initialise Pacific border
        for j in range(n):
            p_que.append((0, j))
            p_seen.add((0, j))
        for i in range(1, m):
            p_que.append((i, 0))
            p_seen.add((i, 0))

        # initialise Atlantic border
        for i in range(m):
            a_que.append((i, n - 1))
            a_seen.add((i, n - 1))
        for j in range(n-1):
            a_que.append((m - 1, j))
            a_seen.add((m - 1, j))

        # BFS inward from a given ocean
        def get_coords(que, seen):
            coords = set()
            while que:
                i, j = que.popleft()
                for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i + i_off, j + j_off
                    # flow only uphill or flat and unseen
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        seen.add((r, c))
                        que.append((r, c))
            
        get_coords(p_que, p_seen)
        get_coords(a_que, a_seen)
        return list(p_seen.intersection(a_seen))

# Time: O(m*n)
# Space: O(m*n)
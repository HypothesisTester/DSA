# Solution: Topological Sorting (BFS)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_cnt = {}
        leaves = deque()
        for source, neighbours in adj.items():
            if len(neighbours) == 1:
                leaves.append(source)
            edge_cnt[source] = len(neighbours)

        # bfs
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neighbour in adj[node]:
                    edge_cnt[neighbour] -= 1
                    if edge_cnt[neighbour] == 1:
                        leaves.append(neighbour)

# Time: O(V + E)
# Space: O(V)
# Where V is the number of vertices and E is the number of edges.
        
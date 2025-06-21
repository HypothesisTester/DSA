class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n     = len(edges)
        parent = list(range(n + 1))
        size   = [1] * (n + 1)   # size[root] = number of nodes in that set

        def find(x: int) -> int:
            """Return root of x with path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> bool:
            """Join the two sets; return False if already in the same set."""
            ra, rb = find(a), find(b)
            if ra == rb:
                return False          # cycle edge

            # union by size
            if size[ra] < size[rb]:
                ra, rb = rb, ra       # make ra the larger root
            parent[rb] = ra
            size[ra]  += size[rb]
            return True

        # scan edges left→right; the first union that returns False is the answer
        for u, v in edges:
            if not union(u, v):
                return [u, v]
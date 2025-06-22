class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        size   = [1] * n

        def find(v: int) -> int:
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra]  += size[rb]
            return True

        provinces = n
        for i in range(n):
            # j starts at i+1 to skip the diagonal and pairs we've already checked
            for j in range(i + 1, n):
                if isConnected[i][j] and union(i, j):
                    provinces -= 1
        return provinces  
        
        
# Time complexity: O(n² * α(n))
# Space complexity: O(n)
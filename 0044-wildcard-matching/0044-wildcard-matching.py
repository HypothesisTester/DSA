class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        NS = len(s)
        NP = len(p)
        cache = [[None] * (NP + 1) for _ in range(NS + 1)]

        def is_match(i, j):
            if cache[i][j] is not None:
                return cache[i][j]

            if i == NS and j == NP:
                cache[i][j] = True
                return True
            
            if j == NP: 
                cache[i][j] = False
                return False
                
            if i == NS: 
                cache[i][j] = (p[j] == "*") and is_match(i, j + 1)
                return cache[i][j]

            if p[j] == "*":
                cache[i][j] = is_match(i, j + 1) or is_match(i + 1, j)

            elif p[j] == "?" or s[i] == p[j]:
                cache[i][j] = is_match(i + 1, j + 1)

            else:
                cache[i][j] = False

            return cache[i][j]

        return is_match(0, 0)


# T: O(NS x NP)
# S: O(NS x NP)
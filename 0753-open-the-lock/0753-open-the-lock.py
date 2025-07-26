class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        if start in dead:
            return -1

        q = deque([(start, 0)]) # [lock, turns]
        seen = {start}

        while q:
            code, turns = q.popleft()
            if code == target:
                return turns

            # for each of the 4 wheels, spin +1 or –1
            for i in range(4):
                digit = int(code[i])
                for delta in (1, -1):
                    nd = (digit + delta) % 10
                    nxt = code[:i] + str(nd) + code[i+1:]
                    if nxt not in dead and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, turns + 1))

        return -1

# Time: O(10^4 * 8) = O(1) practically, but more generally O(10^L * L)
# Space: O(10^4) = O(1) practically, or O(10^L) to store visited codes
        
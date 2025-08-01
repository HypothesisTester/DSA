# Solution: Greedy (two queues)
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)

        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
            
        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if rTurn < dTurn:
                R.append(rTurn + len(senate))
            else:
                D.append(dTurn + len(senate))
        
        return "Radiant" if R else "Dire"

# Time Complexity: O(n) — each senator is enqueued/dequeued at most once per duel  
# Space Complexity: O(n) — for the two index queues  
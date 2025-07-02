# Solution 1: Sort-and-Greedy Lead-Time 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort cars by starting position, farthest first
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        lead_time = 0.0

        for pos, spd in cars:
            time = (target - pos) / spd
            # if this car takes strictly longer than
            # the fleet in front, it forms a new fleet
            if time > lead_time:
                fleets += 1
                lead_time = time

        return fleets

# Time: O(n log n) 
# Space: O(n)

"""
# Solution 2: Sorted Array
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        for p, s in sorted(pair)[::-1]: # Reverse Sorted Order
            stack.append((target - p) / s) # Decimal division
            if len stack >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# Time: O(n log n) 
# Space: O(n) 
"""